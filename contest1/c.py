import sys
import heapq

def main():
    heap = []

    blocks_in_use = 0

    for query in sys.stdin:
        query = query.split()
        
        time = int(query[0])
        if query[1] == "+":
            if not heap or heap[0][0] > time:
                blocks_in_use += 1
                block = blocks_in_use
            else:
                _, block = heapq.heappop(heap)
            heapq.heappush(heap, (time + 600, block))
            # print(block, time + 600)
            print(block)
        else:
            block_id = int(query[2])
            change = "-"
            for i, (end, b) in enumerate(heap):
                if b == block_id and end > time:
                    heap[i] = (time + 600, b)
                    change = "+"
                    # print("+", b, time + 600)
                    heapq.heapify(heap)
                    break
            print(change)




    


if __name__ == "__main__":
    main()