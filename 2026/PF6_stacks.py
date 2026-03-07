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
    print(f"{item} has been added to the stack.")

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
# Main program (example usage)
# -----------------------------

my_stack = create_stack()

# Push elements onto the stack
push(my_stack, "1")
push(my_stack, "2")
push(my_stack, "3")
push(my_stack, "4")

# Display the stack
print("\nCurrent stack:", list(my_stack))

# Peek at the top item
print("\nTop of stack (peek):", peek(my_stack))

# Pop an element
pop(my_stack)

# Peek again after popping
print("\nTop of stack after pop (peek):", peek(my_stack))

# Display the stack after popping
print("\nStack after popping:", list(my_stack))

# Optional: Check if stack is empty
print("\nIs the stack empty?", check_empty(my_stack))