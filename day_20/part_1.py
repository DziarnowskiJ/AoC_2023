from abc import ABC, abstractmethod

with open('../inputs/real/input_day_20.txt', 'r') as file:
    lines = file.readlines()

with open('../inputs/sample/sample_input_day_20_2.txt', 'r') as file:
    sample_lines = file.readlines()


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

    lo_sig = 0
    hi_sig = 0

    for i in range(1000):
        # print('NEW CYCLE', i)
        queue = [('broadcaster', 0, 'button')]
        while len(queue) > 0:
            to_switch, signal, from_switch = queue.pop(0)
            # print(f'{from_switch} --> {to_switch}  ({signal})')
            if signal == 1:
                hi_sig += 1
            elif signal == 0:
                lo_sig += 1
            if to_switch in switches.keys():
                switches[to_switch].input(from_switch, signal)
                signal, send_to, send_from = switches[to_switch].output()
                # print('next:', send_to, signal)
                for tsw in send_to:
                    queue.append((tsw, signal, send_from))
    print(lo_sig, hi_sig)
    return lo_sig * hi_sig


print("Sample output:", process(sample_lines))
print("Answer:", process(lines))
