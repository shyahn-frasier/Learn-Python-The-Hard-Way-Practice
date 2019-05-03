## Animal is-a object
class Animal(object):
    pass

## class Dog is-a Animal that has-a __init__ that takes the params self and name
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name of some kind
        self.name = name

## class Cat is-a Animal that has-a __init__ that takes the params self and name
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name of some kind
        self.name = name

## class Person is-a class of type object that has-a __init__ that takes the params self and name
class Person(object):

    def __init__(self, name):
        ## Person has-a name of some kind
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a person that has-a __init__ that takes the params self, name, and salary
class Employee(Person):

    def __init(self, name, salary):
        ## __init__ has a super function that takes the params Employee and self that has-a attribute __init__ that takes the name param
        super(Employee, self).__init__(name)
        ## Person has a salary of some kind
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet called satan
mary.pet = satan

## frank is-a Employee that takes the params Frank and 120000
frank = Employee("Frank", 120000)

## frank has-a pet called rover
frank.pet = rover

## flipper is-a instance of class Fish
flipper = Fish()

## crouse is-a instance of class Salmon
crouse = Salmon()

## harry is-a instance of class Halibut
harry = Halibut()