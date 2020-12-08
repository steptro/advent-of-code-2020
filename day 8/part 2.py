with open('input.txt', 'r') as f:
    data = list(f.read().split("\n"))


def terminates(d, index):
    current_instruction = 0
    executed_instructions = set()

    accumulator = 0

    while current_instruction not in executed_instructions:
        if current_instruction >= len(d):
            print('acc: ' + str(accumulator))
            return True

        executed_instructions.add(current_instruction)

        execution = d[current_instruction][0:3]
        value = int(d[current_instruction][3:])

        if index == current_instruction:
            if execution == 'jmp':
                current_instruction += 1
            elif execution == 'acc':
                accumulator += value
                current_instruction += 1
            elif execution == 'nop':
                current_instruction += value
        else:
            if execution == 'nop':
                current_instruction += 1
            elif execution == 'acc':
                accumulator += value
                current_instruction += 1
            elif execution == 'jmp':
                current_instruction += value

    return False


lst = []

for i in range(0, len(data)):
    execution = data[i][0:3]

    if execution == 'nop' or execution == 'jmp':
        lst.append(i)


for k in lst:
    terminates(data, k)

