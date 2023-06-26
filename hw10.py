# Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

class Animal:

    def __init__(self, age = 0, weight = 0, name = 'xxx'):
        self.age = age
        self.weight = weight
        self.name = name

    def __str__(self):
        return f'{self.age = } {self.weight = } {self.name =}'

class Fish(Animal):

    def __init__(self, age, weight, name, sea_or_river = 'unknown'):
        super().__init__(age, weight, name)
        self.sea_or_river = sea_or_river

class Dog(Animal):

    def __init__(self, age, weight, name, size= 'small'):
        super().__init__(age, weight, name, size)
        self.size = size

class Bird(Animal):

    def __init__(self, age, weight, name, can_fly = True):
        super().__init__(age, weight, name)
        self.can_fly = can_fly

class Factory(Fish, Dog, Bird):

    def __init__(self, kind_of_animal, age, weight, name, *args):
        match kind_of_animal:
            case 'Fish':
                Fish.__init__(self, age, weight, name, *args)
                self.kind_of_animal = kind_of_animal
            case 'Dog':
                Dog.__init__(self, age, weight,name, *args)
                self.kind_of_animal = kind_of_animal
            case 'Bird':
                Bird.__init__(self, age,weight,name, *args)
                self.kind_of_animal = kind_of_animal

    def __str__(self):
        match self.kind_of_animal:
            case 'Fish':
                return f'возраст {self.age}, вес {self.weight}, имя {self.name}, где живет - {self.sea_or_river}'
        match self.kind_of_animal:
            case 'Dog':
                return f'возраст {self.age}, вес {self.weight}, имя {self.name}, размер - {self.size}'
        match self.kind_of_animal:
            case 'Bird':
                return f'возраст {self.age}, вес {self.weight}, имя {self.name}, может летать? - {self.can_fly}'


creature1 = Factory('Dog', 5, 4, 'Тузик', 'большой')
creature2 = Factory('Fish', 666, 99, 'Щука', 'вода')
creature3 = Factory('Bird', 4, 1, 'Кеша', False)
print(creature1)
print(creature2)
print(creature3)
