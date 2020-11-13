import sys

def operation(left, right, kind):
    if kind == "*":
        return left * right
    elif kind == "+":
        return left + right
    else:
        return left - right

def main():
    stack = []
    operations = sys.stdin.readline().split()

    for char in operations:
        if char in ("*", "-", "+"):
            left, right = stack.pop(), stack.pop()
            stack.append(operation(right, left, char))
        else:
            stack.append(int(char))
    print(stack.pop())


if __name__ == "__main__":
    main()