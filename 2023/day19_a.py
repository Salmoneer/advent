import re

raw_flows, raw_parts = [x.strip().split("\n") for x in open("data/19").read().split("\n\n")]

flows = {}

for flow in raw_flows:
    flow_regex = re.match(r"([a-z]+)\{(.*)\}", flow)

    if flow_regex is None:
        raise Exception("Regex is None")

    name = flow_regex.group(1)
    raw_rules = flow_regex.group(2)

    flows[name] = []
    
    for rule in raw_rules.split(","):
        rule_regex = re.match(r"([x|m|a|s])(\>|\<)(\d+):(.*)", rule)

        if rule_regex is None:
            flows[name].append(rule)
        else:
            flows[name].append([rule_regex.group(i) for i in range(1, 5)])

parts = []

for part in raw_parts:
    part_regex = re.match(r"{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}", part)

    if part_regex == None:
        raise Exception("Regex in None")

    parts.append({"x": int(part_regex.group(1)),
                  "m": int(part_regex.group(2)),
                  "a": int(part_regex.group(3)),
                  "s": int(part_regex.group(4))})

def run_flow(flow, part):
    for rule in flow:
        if type(rule) is str:
            return rule
        else:
            if rule[1] == "<":
                if part[rule[0]] < int(rule[2]):
                    return rule[3]
            else:
                if part[rule[0]] > int(rule[2]):
                    return rule[3]

    raise Exception("Couln't determine result of flow")

valid_parts = []

for part in parts:
    current_flow = "in"
    while current_flow not in ["A", "R"]:
        current_flow = run_flow(flows[current_flow], part)

    if current_flow == "A":
        valid_parts.append(part)

s = 0

for part in valid_parts:
    for k in part:
        s += part[k]

print(s)
