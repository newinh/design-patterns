from abc import ABC, abstractmethod

class Duck(object):

    def __init__(self, fly_behavior: 'FlyBehavior', quack_behavior: 'QuackBehavior'):
        self._fly_behavior = fly_behavior
        self._quack_behavior = quack_behavior

    
    def swim(self):
        print("Swimming....")

    def display(self):
        raise NotImplementedError()

    @property
    def fly_behavior(self):
        return self._fly_behavior
    
    @fly_behavior.setter
    def fly_behavior(self, value: 'FlyBehavior'):
        self._fly_behavior = value

    @property
    def quack_behavior(self):
        return self._quack_behavior
    
    @quack_behavior.setter
    def quack_behavior(self, value: 'QuackBehavior'):
        self._quack_behavior = value

    def perform_quack(self):
        self.quack_behavior.quack()

    def perform_fly(self):
        self.fly_behavior.fly()

class FlyBehavior(ABC):
    
    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):

    def fly(self):
        print("Wing fly")


class FlyNoWay(FlyBehavior):

    def fly(self):
        print("Can't fly")


class QuackBehavior(ABC):

    @abstractmethod
    def quack(self):
        pass


class Quack(QuackBehavior):

    def quack(self):
        print("quack")


class Squeak(QuackBehavior):

    def quack(self):
        print("squeak")


class MuteQuack(QuackBehavior):

    def quack(self):
        pass

class MallardDuck(Duck):

    def display(self):
        return super().display()


if __name__ == '__main__':
    mallard_duck = MallardDuck(fly_behavior=FlyWithWings(),
                               quack_behavior=Quack())
    mallard_duck.perform_fly()
    mallard_duck.perform_quack()

    mallard_duck.quack_behavior = Squeak()
    mallard_duck.perform_quack()
