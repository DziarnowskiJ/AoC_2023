import tokenize
from io import BytesIO

def tokens(text):
    tok = tokenize.tokenize(text.readline)
    name_tuples = [
        (tokenize.tok_name[token.type],
         (int(token.string) if token.type == tokenize.NUMBER else token.string))
        for token in tok
        if token.type not in {tokenize.ENCODING, tokenize.NEWLINE, tokenize.ENDMARKER, tokenize.NL}]
    text.seek(0)

    lines = dict()

    lines[name_tuples[0][1]] = [tok[1] for tok in name_tuples[2:]]

    return lines
    

with open('../inputs/real/input_day_25.txt', 'r') as file:
    lines = file.readlines()
    encoded_lines = [BytesIO(line.encode('utf-8')) for line in lines]
    token_lines = [tokens(encoded_line) for encoded_line in encoded_lines]

with open('../inputs/sample/sample_input_day_25.txt', 'r') as file:
    sample_lines = file.readlines()
    encoded_sample_lines = [BytesIO(line.encode('utf-8')) for line in sample_lines]
    token_sample_lines = [tokens(encoded_line) for encoded_line in encoded_sample_lines]


def remove_edge(full_graph: dict[str, [str]], node1: str, node2: str):
    full_graph[node1].remove(node2)
    full_graph[node2].remove(node1)


def get_nodes(full_graph: dict[str, [str]], node: str):
    queue = [node]
    included = set()

    while len(queue) > 0:
        node = queue.pop(0)
        included.add(node)
        for new_node in full_graph[node]:
            if new_node not in included:
                queue.append(new_node)

    return included

    
def process(tokens_line, edges_to_remove):
    # print edges to use in visual graphs
    for token in tokens_line:
        for node, conn in token.items():
            for cn in conn:
                # graphviz
                # print(f'{node}->{cn} [tooltip="{node}->{cn}"]')
                # mermaid
                print(f'{node}-->{cn};')

    full_graph = dict()
    for token in tokens_line:
        for node, conn in token.items():
            for cn in conn:
                if node not in full_graph.keys():
                    full_graph[node] = [cn]
                else:
                    full_graph[node].append(cn)
                if cn not in full_graph.keys():
                    full_graph[cn] = [node]
                else:
                    full_graph[cn].append(node)

    for edge in edges_to_remove:
        remove_edge(full_graph, edge[0], edge[1])

    included_1 = get_nodes(full_graph, edges_to_remove[0][0])
    included_2 = get_nodes(full_graph, edges_to_remove[0][1])

    return len(included_1) * len(included_2)


print("Sample output:", process(token_sample_lines, [('hfx', 'pzl'), ('bvb', 'cmg'), ('nvd', 'jqt')]))
print("Answer:", process(token_lines, [('kfr', 'vkp'), ('qpp', 'vnm'), ('rhk', 'bff')]))


# https://www.devtoolsdaily.com/graphviz/
# kfr -- vkp
# qpp -- vnm
# rhk -- bff