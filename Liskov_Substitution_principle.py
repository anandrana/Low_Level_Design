# # Bad Example
# class Bird:
#     def fly(self):
#         pass

# class Ostrich(Bird):
#     def fly(self):
#         raise NotImplementedError("Ostrich can't fly")

class Bird:
    def __init__(self, name):
        self.name = name

# Subclass for birds that can fly
class FlyingBird(Bird):
    def fly(self):
        print(f"{self.name} is flying!")

# Subclass for birds that cannot fly (like Ostrich)
class Ostrich(Bird):
    def walk(self):
        print(f"{self.name} is walking.")

# Creating objects from subclasses
sparrow = FlyingBird("Sparrow")
ostrich = Ostrich("Ostrich")

# Calling subclass-specific methods
sparrow.fly()      # Output: Sparrow is flying!
ostrich.walk()     # Output: Ostrich is walking.
