import sys
from math import inf


def push(stack, key):
    if not stack:
        stack.append((key, key))
    else:
        stack.append((key, min(key, stack[-1][1])))


def pop(push_stack, pop_stack):
    if not pop_stack:
        while push_stack:
            push(pop_stack, push_stack.pop()[0])
    return pop_stack.pop()[0]


def queue_min(push_stack, pop_stack):
    push_min = inf if not push_stack else push_stack[-1][1]
    pop_min = inf if not pop_stack else pop_stack[-1][1]

    qmin = min(push_min, pop_min)

    return -1 if qmin == inf else qmin


def main():
    q = int(sys.stdin.readline())
    push_stack, pop_stack = [], []

    for _ in range(q):
        operation = sys.stdin.readline().split()
        if operation[0] == "-":
            pop(push_stack, pop_stack)
        else:
            push(push_stack, int(operation[1]))
    
        sys.stdout.write(str(queue_min(push_stack, pop_stack)) + "\n")


if __name__ == "__main__":
    main()


