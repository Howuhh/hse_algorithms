import sys

def if_possible(ropes, rlen, K):
    count = 0 

    for rope in ropes:
        count += (rope // rlen)

        if count >= K:
            return True

    return False


def find_max(ropes, K):
    left, right = 1, max(ropes)

    max_len = 0
    while left <= right:
        mid = (left + right) // 2

        if if_possible(ropes, mid, K):
            max_len = max(max_len, mid)
            left = mid + 1
        else:
            right = mid - 1

    return max_len


def main():
    n, k = map(int, sys.stdin.readline().split())

    ropes = []
    for _ in range(n):
        ropes.append(int(sys.stdin.readline()))
    
    # ropes.sort()

    print(find_max(ropes, k))


if __name__ == "__main__":
    main()
