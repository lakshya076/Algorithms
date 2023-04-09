'''
A stack is a linear data structure that follows the principle of Last In First Out (LIFO). This means the last element inserted inside the stack is removed first.

There are some basic operations that allow us to perform different actions on a stack.

    Push: Add an element to the top of a stack
    Pop: Remove an element from the top of a stack
    IsEmpty: Check if the stack is empty
    IsFull: Check if the stack is full
    Peek: Get the value of the top element without removing it

The push and pop operations take constant time, i.e. O(1).

'''
# Stack implementation in python


# Creating a stack
def create_stack():
    stack = []
    return stack


# Creating an empty stack
def check_empty(stack):
    return len(stack) == 0


# Adding items into the stack
def push(stack, item):
    stack.append(item)
    # print("pushed item: " + item)


# Removing an element from the stack
def pop(stack):
    if (check_empty(stack)):
        return "Stack is empty"

    return stack.pop()


stack = create_stack()

push(stack, 1)
push(stack, 2)
push(stack, 3)
push(stack, 4)

print(stack)
print(f"Popped item: {pop(stack)}")
print(f"Stack after popping an element: {(stack)}")
