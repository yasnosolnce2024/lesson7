class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self):
        return "Птицы издают звук: Чирик-чирик"

    def eat(self):
        return "Птицы едят зерно и червей"

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return "Млекопитающие издают различные звуки"

    def eat(self):
        return "Млекопитающие едят мясо, траву, фрукты и т.д."

class Reptile(Animal):
    def __init__(self, name, age, skin_type):
        super().__init__(name, age)
        self.skin_type = skin_type

    def make_sound(self):
        return "Рептилии обычно не издают звуков"

    def eat(self):
        return "Рептилии едят мясо, рыбу и т.д."

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff):
        self.staff.append(staff)

class ZooKeeper:
    def feed_animal(self, animal):
        return f"Смотритель кормит животное {animal.name}"

class Veterinarian:
    def heal_animal(self, animal):
        return f"Ветеринар лечит животное {animal.name}"

def animal_sound(animals):
    for animal in animals:
        print(f"{animal.name} издает звук: {animal.make_sound()}")


