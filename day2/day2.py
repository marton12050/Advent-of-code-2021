def task1(data):
    depth = 0
    forward = 0
    for cmd in data:
        command, arg = cmd.split(" ")
        if command == "forward":
            forward += int(arg)
        elif command == "down":
            depth += int(arg)
        else:
            depth -= int(arg)
    return depth*forward


def task2(data):
    depth = 0
    forward = 0
    aim = 0
    for cmd in data:
        command, arg = cmd.split(" ")
        if command == "forward":
            forward += int(arg)
            depth += aim * int(arg)
        elif command == "down":
            aim += int(arg)
        else:
            aim -= int(arg)
    return depth * forward


data = open("input.txt", "r").read().splitlines()
print(task1(data))
print(task2(data))