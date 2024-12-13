import math
from abc import ABC, abstractmethod

with open('../inputs/real/input_day_20.txt', 'r') as file:
    lines = file.readlines()


def lcm(a, b):
    return int(a * b / math.gcd(a, b))


def lcm_arr(arr):
    val = arr[0]
    for v in arr:
        val = lcm(val, v)
    return val


class Switch(ABC):
    def __init__(self, send_to, name):
        self.send_to = send_to
        self.state = None
        self.name = name

    @abstractmethod
    def input(self, switch, signal):
        pass

    @abstractmethod
    def output(self):
        pass


class Broadcast(Switch):
    def __init__(self, send_to, name):
        super().__init__(send_to, name)

    def input(self, switch, signal):
        self.state = signal

    def output(self):
        return self.state, self.send_to, self.name


class Conjunction(Switch):
    def __init__(self, send_to, name):
        super().__init__(send_to, name)
        self.last_pulse = dict()

    def add_pulse(self, connection):
        self.last_pulse[connection] = 0
    # def init_pulses(self, connections):
    #     for connection in connections:
    #         self.last_pulse[connection] = 0

    def input(self, switch, signal):
        self.last_pulse[switch] = signal

    def output(self):
        output_signal = int(not all([val for val in self.last_pulse.values()]))
        return output_signal, self.send_to, self.name


class Flipflop(Switch):
    def __init__(self, send_to, name):
        super().__init__(send_to, name)
        self.turn_on = False

    def input(self, switch, signal):
        self.state = signal
        if signal == 0:
            self.turn_on = not self.turn_on

    def output(self):
        if self.state == 1:
            return None, [], self.name
        elif self.state == 0:
            return int(self.turn_on), self.send_to, self.name


class Button(Switch):
    def __init__(self, name):
        super().__init__(['broadcaster'], name)
        self.state = 0

    def input(self, switch, signal):
        self.state = 0

    def output(self):
        return 0, self.send_to, self.name


def switch_creator(switch_type, send_to=None, name=None):
    if switch_type == 'B':
        return Broadcast(send_to, name)
    elif switch_type == 'C':
        return Conjunction(send_to, name)
    elif switch_type == 'F':
        return Flipflop(send_to, name)
    elif switch_type == 'S':
        return Button(name)
    else:
        raise Exception('Unrecognized switch type')


def get_switches(lines):
    switches = {'button': switch_creator('S', name='button')}

    conjunctions = []
    for line in lines:
        l, r = line.split(' -> ')[:2]

        send_to = r.strip().split(', ')
        if l.startswith('broadcaster'):
            name = l
            switch = switch_creator('B', send_to, l)
        elif l.startswith('&'):
            name = l[1:]
            switch = switch_creator('C', send_to, l[1:])
            conjunctions.append(name)
        elif l.startswith('%'):
            name = l[1:]
            switch = switch_creator('F', send_to, l[1:])
        else:
            raise Exception(f'Passed {l} as switch')

        switches[name] = switch

    for switch in switches.values():
        for dest in switch.send_to:
            if dest in conjunctions:
                switches[dest].add_pulse(switch.name)

    return switches


def process(lines):
    switches = get_switches(lines)

    counter = 0
    # Ultimate switches found with:
    # https://dreampuf.github.io/GraphvizOnline/#digraph%20G%20%7B%0A%0Avb%20-%3E%20ck%0Apb%20-%3E%20xv%0Agt%20-%3E%20jq%0Ahj%20-%3E%20lk%2C%20hh%0Azd%20-%3E%20fm%0Ahr%20-%3E%20hh%0Arg%20-%3E%20tp%0Atf%20-%3E%20ck%2C%20tx%0App%20-%3E%20vs%2C%20hh%0Avx%20-%3E%20df%0Atx%20-%3E%20mr%2C%20ck%0Anh%20-%3E%20vx%0Asc%20-%3E%20ck%2C%20vb%0Acc%20-%3E%20ck%2C%20rj%0Atn%20-%3E%20kz%2C%20lt%0Afp%20-%3E%20rb%0Ahc%20-%3E%20kz%0Arb%20-%3E%20ns%2C%20mf%0Apc%20-%3E%20vh%0Astart%20-%3E%20tf%2C%20br%2C%20zn%2C%20nc%0Azn%20-%3E%20kz%2C%20fv%0Ans%20-%3E%20pb%2C%20lr%2C%20br%2C%20fp%2C%20gp%2C%20gv%2C%20jl%0Anc%20-%3E%20hh%2C%20hj%0Amf%20-%3E%20ns%2C%20gp%0Axv%20-%3E%20ns%2C%20kh%0Arj%20-%3E%20ck%2C%20sc%0Atg%20-%3E%20cc%0Agp%20-%3E%20pb%0Ajz%20-%3E%20lj%2C%20ns%0Ajl%20-%3E%20fp%0Avr%20-%3E%20jq%0Ajq%20-%3E%20end%0Akz%20-%3E%20zf%2C%20nl%2C%20df%2C%20zn%2C%20vx%2C%20nh%0Agv%20-%3E%20jl%0Agf%20-%3E%20zf%2C%20kz%0Adf%20-%3E%20gf%0Akq%20-%3E%20pp%0Alk%20-%3E%20hh%2C%20zd%0Avs%20-%3E%20bp%0Alt%20-%3E%20ls%2C%20kz%0Anl%20-%3E%20jq%0Amr%20-%3E%20rg%0Azf%20-%3E%20qf%0Abr%20-%3E%20gv%2C%20ns%0Ark%20-%3E%20hh%2C%20hr%0Aqf%20-%3E%20kz%2C%20tn%0Arv%20-%3E%20rk%2C%20hh%0Als%20-%3E%20hc%2C%20kz%0Afm%20-%3E%20kq%0Ack%20-%3E%20tp%2C%20vr%2C%20pc%2C%20tg%2C%20mr%2C%20tf%2C%20rg%0Afv%20-%3E%20nh%2C%20kz%0Atp%20-%3E%20pc%0Avh%20-%3E%20ck%2C%20tg%0Ahh%20-%3E%20vs%2C%20kq%2C%20gt%2C%20nc%2C%20zd%2C%20fm%0Alr%20-%3E%20jq%0Akh%20-%3E%20ns%2C%20jz%0Abp%20-%3E%20hh%2C%20rv%0Alj%20-%3E%20ns%0A%0A%20%20start%20%5Bshape%3DMdiamond%5D%3B%0A%20%20end%20%5Bshape%3DMsquare%5D%3B%0A%7D
    ultimate_switches = {
        'nl': [],
        'vr': [],
        'lr': [],
        'gt': []
    }
    run = True
    while run:
        queue = [('broadcaster', 0, 'button')]
        counter += 1
        while len(queue) > 0:
            to_switch, signal, from_switch = queue.pop(0)
            if to_switch in switches.keys():
                switches[to_switch].input(from_switch, signal)
                signal, send_to, send_from = switches[to_switch].output()
                for tsw in send_to:
                    if tsw in ultimate_switches.keys() and signal == 0:
                        ultimate_switches[tsw].append(counter)
                        if all([len(val) >= 2 for val in ultimate_switches.values()]):
                            run = False
                    queue.append((tsw, signal, send_from))

    cycles = [val[1] - val[0] for val in ultimate_switches.values()]
    return lcm_arr(cycles)


print("Answer:", process(lines))
