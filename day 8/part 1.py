with open('input.txt', 'r') as f:
    data = list(f.read().split("\n"))

current_instruction = 0
executed_instructions = set()

accumulator = 0

while current_instruction not in executed_instructions:
    executed_instructions.add(current_instruction)
    execution = data[current_instruction][0:3]
    value = int(data[current_instruction][3:])

    if execution == 'nop':
        current_instruction += 1
    elif execution == 'acc':
        accumulator += value
        current_instruction += 1
    elif execution == 'jmp':
        current_instruction += value

print(accumulator)  # 1727
