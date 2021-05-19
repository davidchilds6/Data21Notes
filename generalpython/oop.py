# # Abstraction is hiding the internal details of how things work.
# # I.E writing 30 lines for a function previously but only using one phrase to call it.
# # User is kept unaware of the basic implementation of a function.

# # Encapsulation is more to do with making things inaccessible by hiding it.
# # Stuff that the user shouldn't be changing is prevented from being visible.

# # Inheritance, sub-classes take from a main class (main class created first)

# # Polymorphism is the ability of an object to take on many forms.
# # This means any child class object can take any form of a class in its parent hierarchy and of course itself as well.
# # Methods of the same name that do different things????

class Animal:

    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("One breath in and one breath out")

    def eat(self):
        print("nom nom nom")

    def moving(self):
        print("forwards, backwards and side to side")


cat = Animal()
# cat.breathe()

# # e.g from animalclass import Animal


class Reptile(Animal):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True

    def use_venom(self):
        print("If i have venom im going to use it")

    def moving(self):
        print("moving but like a snake instead")  # This overides the original moving class from the parent (Animal)


bob = Reptile()
# bob.use_venom()
# bob.moving()
# cat.moving()
# bob.breathe()

# When a method is used in its own file............
# # https://www.freecodecamp.org/news/if-name-main-python-example/
# if __name__ == '__main__':
#     cat = Animal()
#     cat.breathe()
#     print(__name__)

# # representation method
# def __repr__(self):
#    return f"This is a reptile"
# print(repr(bob))

# def __str__(self):
#    return f"str version of this is a reptile"

