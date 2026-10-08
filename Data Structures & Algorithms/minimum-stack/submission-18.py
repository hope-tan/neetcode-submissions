# clarifications
    # empty? no
    # well formed input (all ints)? yes

class MinStack:

    def __init__(self):
        # intitialize stack object
        # list of values
        # list of mins
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # push val onto the stack
        # list.append
        # if new val < minStack[-1]
        # add new val to minStack

        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        # remove the top element
        # remove list[-1]
        # if the value getting popped off stack == top value on minStack
            # pop minStack and the stack
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        # retrieve the top element
        # return list[-1]
        return self.stack[-1]

    def getMin(self) -> int:
        # retrieve the min element in the stack
        # brute force: iterate through everything in the list with a variable to track min
            # if l in list is less than current min
                # update the min to the new min
            # return the last min after iterating through everything
        # return minStack[-1]
        return self.minStack[-1]
