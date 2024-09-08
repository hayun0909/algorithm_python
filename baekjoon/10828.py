N = int(input())
stack = []
result_print = []

for i in range(N):
    command = input()
    if 'push' in command:
        _, num = command.split()
        stack.append(int(num))
    elif 'pop' in command:
        if len(stack) == 0:
            result_print.append(-1)
        else:
            remove = stack.pop()
            result_print.append(remove)
    elif 'size' in command:
        result_print.append(len(stack))
    elif 'empty' in command:
        if len(stack) == 0:
            result_print.append(1)
        else:
            result_print.append(0)
    elif 'top' in command:
        if len(stack) == 0:
            result_print.append(-1)
        else:
            result_print.append(stack[-1])

for result in result_print:
    print(result)