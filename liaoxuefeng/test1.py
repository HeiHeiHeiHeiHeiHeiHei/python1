class Animal:
    def run(self):
        print('Animal is running')
    def run_twice(self,animal):
        animal.run()


class Dog(Animal):
    def run(self):
        print('dog is running')
    def run_twice(self,animal):
        animal.run()


class Cat(Animal):
    def run(self):
        print('cat is running')

class Plant():
    def run(self):
        print('plant is running')

dog=Dog()
cat=Cat()
dog.run()
cat.run()
animal=Animal()
animal.run_twice(cat)
dog.run_twice(cat)
plant=Plant()
dog.run_twice(plant)
cat.run_twice(cat)

