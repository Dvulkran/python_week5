
# %%
# Base class (optional for structure, not required for polymorphism)
class Entity:
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")


# Vehicle classes with unique move() implementations
class Car(Entity):
    def move(self):
        print("Driving on the highway 🚗")


class Plane(Entity):
    def move(self):
        print("Flying through the clouds ✈️")


class Boat(Entity):
    def move(self):
        print("Sailing across the ocean 🚢")


# Animal classes with unique move() implementations
class Dog(Entity):
    def move(self):
        print("Running in the park 🐕")


class Bird(Entity):
    def move(self):
        print("Soaring in the sky 🐦")


class Fish(Entity):
    def move(self):
        print("Swimming in the reef 🐠")


# Polymorphic behavior: same method, different results
def show_movement(entities):
    for entity in entities:
        entity.move()


# Create instances of each class
entities = [
    Car(),
    Plane(),
    Boat(),
    Dog(),
    Bird(),
    Fish()
]

# Demonstrate polymorphism
show_movement(entities)

# %%
