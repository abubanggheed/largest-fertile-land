from largest_fertile_land import largest_fertile

inputs = [
    '5 6\nFBBFFB\nFBFFBB\nFFBBFF\nBBFBFF\nBFBBFF\n4\n1 3\n2 4\n1 5\n3 5'
]

expected_outputs = [
    '3\n4\n6\n6\n'
]

outputs = []
for i in range(0, len(inputs)):
    outputs.append(largest_fertile(inputs[i]))

for i in range(0, len(outputs)):
    print(outputs[i] == expected_outputs[i])