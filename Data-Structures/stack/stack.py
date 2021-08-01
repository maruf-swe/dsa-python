class Stack:
    def __init__(self, max_size):
        self.top_pointer = -1
        self.stack = [None for _ in range(max_size)]
        self.max_size = max_size

    def push(self, new_element):
        self.top_pointer = self.top_pointer + 1
        self.stack[self.top_pointer] = new_element

    def pop(self):
        last_element = self.stack[self.top_pointer]
        self.top_pointer = self.top_pointer - 1
        return last_element

    def peek(self):
        return self.stack[self.top_pointer]

    def is_empty(self):
        return self.top_pointer == -1

    def is_full(self):
        return len(self.stack) == self.max_size


s1 = Stack(5)
s1.push('A')
s1.push('B')
s1.push('C')
s1.push('D')
s1.push('F')
print(s1.peek())
print(s1.is_empty())
print(s1.is_full())
