class Kangaroo:
    def __init__(self):
        # Initialize an empty list for pouch contents
        self.pouch_contents = []

    def put_in_pouch(self, item):
        # Add the item to the pouch
        self.pouch_contents.append(item)

    def __str__(self):
        # Return a string representation of the Kangaroo and its pouch contents
        contents = ', '.join(str(item) for item in self.pouch_contents)
        return f"Kangaroo with pouch contents: [{contents}]"

# Testing the Kangaroo class
kanga = Kangaroo()  # Create a Kangaroo object named kanga
roo = Kangaroo()    # Create another Kangaroo object named roo

# Add roo to kanga's pouch
kanga.put_in_pouch(roo)

# Print the string representation of kanga
print(kanga)  # Output: Kangaroo with pouch contents: [Kangaroo with pouch contents: []]
