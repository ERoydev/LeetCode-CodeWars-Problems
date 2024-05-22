def calc(expr):
    if not expr.strip():
        return 0

    args = expr.split()
    queue = []

    for i in args:
        if i.replace('.', '', 1).isdigit():
            queue.append(float(i))

        else:
            b = queue.pop()
            a = queue.pop()
            result = 0

            if i == '+':
                result = a + b

            elif i == '*':
                result = a * b

            elif i == '-':
                result = a - b

            elif i == '/':
                result = a / b

            queue.append(result)

    end = queue[0]
    if end % 1 == 0:
        end = int(end)
    return end


print(calc('5 1 2 + 4 * + 3 -'))

