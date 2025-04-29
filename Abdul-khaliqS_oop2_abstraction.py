from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class Lamp(Appliance):
    def turn_on(self):
        print("Lamp turned on");

class Fan(Appliance):
    def turn_on(self):
        print("Fan turned on")

class Washing_Machine(Appliance):
    def turn_on(self):
        print("Machine turned on")

my_lamp = Lamp()
my_lamp.turn_on()

my_fan = Fan()
my_fan.turn_on()

my_machine = Washing_Machine()
my_machine.turn_on()