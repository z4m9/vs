# Logical Python - Animals
# Created by Samuel Marriott of 3/04/2026

# Facts
facts = {
    'mammal': ['dog', 'cat', 'whale', 'squirrel'], # Added: squirrel
    'bird': ['sparrow', 'eagle', 'penguin'],
    'can_walk': ['dog', 'cat', 'penguin'],
    'can_fly': ['sparrow', 'eagle'],
    'has_fur': ['dog', 'cat', 'squirrel'], # Added: squirrel
    'lives_in_water': ['whale', 'penguin', 'snake', 'lizard'], # Added: snake, lizard
    'can_climb': ['squirrel', 'snake', 'lizard'], # Added
    'reptile': ['snake', 'lizard'] # Added
}

# Rules
def can_swim(animal):
    return animal in facts['lives_in_water']
def can_walk(animal):
    return animal in facts['can_walk']

def can_fly(animal):
    return animal in facts['can_fly']

def can_climb(animal):
    return animal in facts['can_climb']

# Knowledge Base
def infer_properties(animal):
    properties = []
    if can_swim(animal):
        properties.append('can swim')
    if can_walk(animal):
        properties.append('can walk')
    if can_fly(animal):
        properties.append('can fly')
    if can_climb(animal): # Added
        properties.append('can climb') # Added
    return properties

# Main program
def main():
    animal = input("Enter the animal you want to query: ").lower()

    if any(animal in category for category in facts.values()):
        print(f"Facts about {animal}:")
        print("Is a mammal:", animal in facts['mammal'])
        print("Is a bird:", animal in facts['bird'])
        print("Can swim:", animal in facts ['lives_in_water'])
        print("Can climb:", animal in facts ['can_climb']) # Added
        print("Is a reptile:", animal in facts ['reptile']) # Added

        print("Inferred properties:")
        properties = infer_properties(animal)
        if properties:
            for prop in properties:
                print("-", prop)
        else:
            print("No inferred properties.")
    else:
        print("Animal not found in the knowledge base.")

if __name__ == "__main__":
    main()