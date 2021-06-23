class Queue:

    def __init__(self):
        self.en = []
        self.out = []

    def enq(self, val):
        self.en.append(val)

    def deq(self):

        if len(self.out) == 0:

            while len(self.en) != 0:

                self.out.append(self.en.pop())

        return self.out.pop()

    def peek(self):

        if len(self.out) == 0:

            while len(self.enq) != 0:

                self.out.append(self.enq.pop())

        return self.out[-1]

    def empty(self):

        return len(self.en) == 0 and len(self.out) == 0


q = Queue()
q.enq(1)
q.enq(2)
q.enq(3)
q.enq(4)
print(q.deq())
