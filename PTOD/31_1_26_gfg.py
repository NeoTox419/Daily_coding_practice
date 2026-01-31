#Problem name: Implement Queue in a Single Array
'''
Intuition:
We need to implement k independent queues using a single array of size n.
To efficiently manage space, we reuse freed positions when elements are dequeued.
This is achieved by maintaining a free list of available indices.

Approach:
1. Use an array `arr` of size n to store all queue elements.
2. Maintain two arrays `front` and `rear` of size k to track the front
   and rear indices of each queue.
3. Use an array `next` of size n:
   - To link elements within the same queue.
   - To maintain a free list of available indices.
4. Maintain a variable `free` that points to the first free index in the array.
5. Enqueue operation:
   - Take an index from the free list.
   - Insert the element and update queue links.
6. Dequeue operation:
   - Remove the front element of the queue.
   - Add the freed index back to the free list.
7. isEmpty checks whether the front of a queue is -1.
8. isFull checks whether the free list is exhausted.

Time Complexity:
- Enqueue: O(1)
- Dequeue: O(1)
- isEmpty: O(1)
- isFull: O(1)

Space Complexity:
- O(n + k)
'''

class kQueues:

    def __init__(self, n, k):
        self.n = n
        self.k = k

        self.arr = [0] * n
        self.front = [-1] * k
        self.rear = [-1] * k

        self.next = [i + 1 for i in range(n)]
        if n > 0:
            self.next[n - 1] = -1

        self.free = 0 if n > 0 else -1

    def enqueue(self, x, i):
        if self.free == -1:
            return

        qi = i - 1
        idx = self.free
        self.free = self.next[idx]

        if self.front[qi] == -1:
            self.front[qi] = idx
        else:
            self.next[self.rear[qi]] = idx

        self.next[idx] = -1
        self.rear[qi] = idx
        self.arr[idx] = x

    def dequeue(self, i):
        qi = i - 1
        if self.front[qi] == -1:
            return -1

        idx = self.front[qi]
        self.front[qi] = self.next[idx]

        if self.front[qi] == -1:
            self.rear[qi] = -1

        self.next[idx] = self.free
        self.free = idx
        return self.arr[idx]

    def isEmpty(self, i):
        return self.front[i - 1] == -1

    def isFull(self):
        return self.free == -1