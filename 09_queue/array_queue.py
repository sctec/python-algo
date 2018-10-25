"""
用数组实现队列 by pillar
"""


class ArrayQueue:

    def __init__(self, capacity):
        self.items = []
        self.capacity = capacity
        self.head = 0
        self.tail = 0

    def __str__(self):
        return "List(%r)" % self.items

    # 入队
    def enqueue(self, item):
        # 队尾没有空间
        if self.tail == self.capacity:
            # 队列已满
            if self.head == 0:
                return False
            else:
                i = self.head
                for i in range(self.head, self.tail):
                    self.items[i - self.head] = self.items[i]
                self.tail -= self.head
                self.head = 0
        self.items.insert(self.tail, item)
        self.tail += 1
        return True

    # 出队
    def dequeue(self):
        # print("1")
        if self.head == self.tail:
            return None
        item = self.items[self.head]
        print(item)
        print("======" + str(self.head))
        self.head += 1
        print("------"+str(self.head))
        self.items = self.items[self.head:self.tail:1]
        print(item)
        print(self.items)
        return item


def main():
    q = ArrayQueue(20)
    for i in range(10):
        q.enqueue(str(i))
    print(q)

    for j in range(3):
        q.dequeue()
        # print(q)
    print(q)

    q.enqueue("7")
    q.dequeue()
    # q.dequeue()
    print(q)


main()
