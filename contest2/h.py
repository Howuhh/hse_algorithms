

def main():
    with open("segments.in", "r") as fin, open("segments.out", "w") as fout:
        n = int(fin.readline())
        segments = []
        
        for i in range(n):
            a, b = map(int, fin.readline().split())
            segments.append((a, b))
        segments.sort(key=lambda t: t[1])

        count, prev = 1, 0
        for i in range(1, n):
            if segments[i][0] >= segments[prev][1]:
                count += 1
                prev = i

        fout.write(str(count))

if __name__ == "__main__":
    main()