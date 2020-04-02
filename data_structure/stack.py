class Stack():
	def __init__(self, max_size):
		self.max_size = max_size
		self.items = [None] * max_size
		
	def push(self, item):
		if self.items[0] == None:
			self.items.remove(self.items[0])
		self.items.append(item)
		if len(self.items) > self.max_size:
			print ('List has exceeded and ' + str(item) + ' cannot be added')
			self.get_stack()
			self.items.remove(self.items[-1])

	def pop(self):
		self.items.insert(0, None)
		if self.peek() != None:
			return self.items.pop()
		else:
			return None

	def is_empty(self):
		return self.items == [None] * self.max_size

	def peek(self):
		if not self.is_empty():
			return self.items[-1]

	def get_stack(self):
		print ('Top')
		stack = self.items[::-1]
		for i in stack:
			print (i)
		print ('Bottom')

def reverse_String(stack, input_str):
	#loop through the string and push contents
	for i in range(len(input_str)):
		stack.push(input_str[i])

	rev_str = ''
	while not stack.is_empty():
		rev_str += stack.pop()

	return rev_str

#stack = Stack()
#input_str = 'Hello World'
#print (reverse_String(stack, input_str))
'''
s = Stack(3)
s.push("A")
s.push("B")
(s.get_stack())
s.push("C")
s.push("D")
(s.get_stack())
s.pop()

(s.get_stack())
'''