
# %%
# Base class representing a generic character
class Character:
    # Constructor initializes common attributes
    def __init__(self, name, origin, catchphrase):
        self.name = name                  # Public attribute
        self.origin = origin              # Public attribute
        self._catchphrase = catchphrase  # Encapsulated (protected) attribute

    # Method common to all characters
    def speak(self):
        return f"{self.name} says: '{self._catchphrase}'"

    # Encapsulation: Getter for catchphrase
    def get_catchphrase(self):
        return self._catchphrase

    # Encapsulation: Setter with validation
    def set_catchphrase(self, new_phrase):
        if isinstance(new_phrase, str) and len(new_phrase) > 0:
            self._catchphrase = new_phrase
        else:
            print("Invalid catchphrase. Must be a non-empty string.")

    # Method to describe character origin
    def describe(self):
        return f"{self.name} hails from {self.origin}."


# Subclass representing a superhero (Inheritance from Character)
class Superhero(Character):
    def __init__(self, name, origin, catchphrase, powers):
        super().__init__(name, origin, catchphrase)  # Constructor chaining
        self.powers = powers  # List of powers (unique to Superhero)

    # Polymorphism: Overrides speak() method
    def speak(self):
        return f"{self.name} (Superhero) shouts: '{self._catchphrase}' 💥"

    # Method unique to Superhero
    def show_powers(self):
        return f"{self.name}'s powers: " + ", ".join(self.powers)


# Subclass representing a villain (Inheritance from Character)
class Villain(Character):
    def __init__(self, name, origin, catchphrase, evil_plan):
        super().__init__(name, origin, catchphrase)  # Constructor chaining
        self.evil_plan = evil_plan  # Unique attribute for Villain

    # Polymorphism: Overrides speak() method
    def speak(self):
        return f"{self.name} (Villain) whispers: '{self._catchphrase}' 😈"

    # Method unique to Villain
    def reveal_plan(self):
        return f"{self.name}'s evil plan: {self.evil_plan}"


# Example usage demonstrating all concepts
hero = Superhero("Photon Blaze", "Neo-Tokyo", "Justice burns brighter!", ["Laser Vision", "Flight", "Time Warp"])
villain = Villain("Shadow Wraith", "Unknown", "Chaos is eternal...", "Unleash the void on Earth")

# Polymorphism in action: same method, different behavior
for character in [hero, villain]:
    print(character.speak())     # Calls overridden speak()
    print(character.describe())  # Inherited method

# Encapsulation: accessing and modifying protected attribute
print(hero.get_catchphrase())   # Getter
hero.set_catchphrase("Light conquers all!")  # Setter with validation
print(hero.speak())             # Updated catchphrase

# Subclass-specific methods
print(hero.show_powers())       # Superhero method
print(villain.reveal_plan())    # Villain method

# %%
