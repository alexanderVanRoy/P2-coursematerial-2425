class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows

    def use_arrows(self, num):
        if num <= self.__num_arrows:
            self.__num_arrows -= num
        else:
            raise ValueError("Not enough arrows")


class Crossbowman(Archer):
    def __init__(self, name, num_arrows):
        super().__init__(name, num_arrows)

    def triple_shot(self, target):
        self.use_arrows(3)
        target_text = " was shot by 3 crossbow bolts" 
        if isinstance(target, Human):
            return f"{target.get_name()}"+target_text
        else:
            return "target" + target_text

crossbowman1 = Crossbowman("Harry", 18)

print(crossbowman1.get_name())
print(crossbowman1.get_num_arrows())

human1 = Human("Mary")

print(crossbowman1.triple_shot(human1))