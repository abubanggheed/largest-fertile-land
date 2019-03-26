from largest_fertile_land import largest_fertile

inputs = [
    '5 6\nFBBFFB\nFBFFBB\nFFBBFF\nBBFBFF\nBFBBFF\n4\n1 3\n2 4\n1 5\n3 5',
    '3 6\nBBFFFF\nFFFFBB\nBBFFBB\n2\n1 3\n2 3',
    '4 8\nFFBBFFFF\nFFFFFFBB\nFFBBFFBB\nFFBBBBBB\n3\n1 4\n1 3\n2 4',
    '2 2\nFB\nBB\n1\n2 2'
]

expected_outputs = [
    '3\n4\n6\n6\n',
    '6\n4\n',
    '8\n6\n6\n',
    '0\n'
]

outputs = []
for i in range(0, len(inputs)):
    outputs.append(largest_fertile(inputs[i]))

passed = 0
for i in range(0, len(outputs)):
    if(outputs[i] == expected_outputs[i]):
        passed += 1
        print('test ' + str(i + 1) + ' of ' + str(len(outputs)) + ' passed')
    else:
        print('test ' + str(i + 1) + ' of ' + str(len(outputs)) + ' failed')
if(passed == len(outputs)):
    print('all tests passed')
else:
    print('not all tests passed')
