import itertools

data = open("data/20").read().splitlines()

Pulse = int
PULSE_HIGH: Pulse = 1
PULSE_LOW: Pulse = 0

class Module:
    name: str
    connections: list[str]
    last_pulses: dict[str, Pulse]

    def recieve_pulse(self, sender: str, pulse: Pulse): ...

class QueueItem:
    def __init__(self, sender: str, reciever: str, pulse: Pulse):
        self.sender = sender
        self.reciever = reciever
        self.pulse = pulse

    def __repr__(self):
        return f"Sender: {self.sender}, Reciever: {self.reciever}, Pulse: {self.pulse}"

modules: dict[str, Module] = {}

pulse_queue: list[QueueItem] = []

class Broadcaster(Module):
    def __init__(self, name: str, connections: list[str]):
        self.name = name
        self.connections = connections

    def recieve_pulse(self, sender: str, pulse: Pulse):
        for module in self.connections:
            pulse_queue.append(QueueItem(self.name, module, pulse))

class FlipFlop(Module):
    def __init__(self, name: str, connections: list[str]):
        self.name = name
        self.connections = connections
        self.state = PULSE_LOW

    def recieve_pulse(self, sender: str, pulse: Pulse):
        if pulse == PULSE_LOW:
            self.state = 1 if self.state == 0 else 0

            for module in self.connections:
                pulse_queue.append(QueueItem(self.name, module, self.state))

class Conjunction(Module):
    def __init__(self, name: str, connections: list[str]):
        self.name = name
        self.connections = connections

        self.last_pulses: dict[str, Pulse] = {}

    def recieve_pulse(self, sender: str, pulse: Pulse):
        self.last_pulses[sender] = pulse

        for name in self.last_pulses:
            if self.last_pulses[name] != PULSE_HIGH:
                for module in self.connections:
                    pulse_queue.append(QueueItem(self.name, module, PULSE_HIGH))

                return

        for module in self.connections:
            pulse_queue.append(QueueItem(self.name, module, PULSE_LOW))

for line in data:
    name, connections = line.split(" -> ")
    connections = connections.split(", ")

    if name == "broadcaster":
        modules[name] = Broadcaster(name, connections)
    elif name.startswith("%"):
        modules[name[1:]] = FlipFlop(name[1:], connections)
    elif name.startswith("&"):
        modules[name[1:]] = Conjunction(name[1:], connections)
    else:
        raise Exception("Parsing error")

for module in modules:
    for nested_module in modules[module].connections:
        if nested_module in modules and type(modules[nested_module]) == Conjunction:
            modules[nested_module].last_pulses[module] = PULSE_LOW

feeder = [x for x in modules if "rx" in modules[x].connections][0]
feeders = [x for x in modules if feeder in modules[x].connections]

s = 1

for i in itertools.count(1):
    pulse_queue.append(QueueItem("button", "broadcaster", PULSE_LOW))

    done = False

    while len(pulse_queue) > 0:
        done = len(feeders) == 0

        current_pulse = pulse_queue.pop(0)

        if current_pulse.sender in feeders and current_pulse.pulse == PULSE_HIGH:
            feeders.remove(current_pulse.sender)
            s *= i

        if current_pulse.reciever in modules:
            modules[current_pulse.reciever].recieve_pulse(current_pulse.sender, current_pulse.pulse)

    if done:
        break

print(s)
