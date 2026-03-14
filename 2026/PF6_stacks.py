# Main program (Task 1: Stack Modification)
# Samuel Marriott - 8/03/2026

from collections import deque  # deque = double-ended queue

# -----------------------------
# Stack operations (using deque)
# -----------------------------

def create_stack():
    """Create and return an empty stack."""
    return deque()

def check_empty(stack):
    """Return True if the stack is empty, otherwise False."""
    return len(stack) == 0

def push(stack, item):
    """Add an item to the top of the stack."""
    stack.append(item)
    print(f"{item} items has been added to the stack.")

def pop(stack):
    """Remove and return the top item from the stack."""
    if check_empty(stack):
        print("Cannot pop: stack is empty.")
        return None
    removed_item = stack.pop()
    print(f"{removed_item} has been removed from the stack.")
    return removed_item

def peek(stack):
    """Return the top item without removing it."""
    if check_empty(stack):
        print("Cannot peek: stack is empty.")
        return None
    return stack[-1]

# -----------------------------
# Main program (Task 1: Stack Modification)
# Samuel Marriott - 8/03/2026
# -----------------------------

my_stack = create_stack()
# The user is asked how many items they would like to push.
items = int(input("How many items would you like to add? "))

# A loop is used to push user-entered values onto the stack.
i = 0
while i < items:
    i += 1
    push(my_stack, i)
    # The stack is printed after each push.
    print("\n Current stack:", list(my_stack))

# peek() is demonstrated before popping.
print("\n Top of stack (peek):", peek(my_stack))

# Two items are popped.
pop(my_stack)
pop(my_stack)

# peek() is demonstrated after popping.
print("\n Top of stack after pop (peek):", peek(my_stack))

# The stack is printed again.
print("\n Current stack:", list(my_stack))

# Attempt to pop once more after the stack becomes empty to demonstrate underflow handling.
pop(my_stack)

# Display the stack after popping
print("\n Stack after popping:", list(my_stack))

# Optional: Check if stack is empty
print("\n Is the stack empty?", check_empty(my_stack))

