class BeeElephant:
    def __init__(self, bee, elephant):
        self.bee = bee
        self.elephant = elephant

    def fly(self):
        return self.bee > self.elephant

    def trumpet(self):
        if self.elephant > self.bee:
            return "tu-tu-doo-doo!"
        else:
            return "wzzzzz"

    def eat(self, meal, value):
        if meal == "nectar":
            self.elephant -= value
            self.bee += value
        elif meal == "grass":
            self.elephant += value
            self.bee -= value

        self.bee = min(100, max(0, self.bee))
        self.elephant = min(100, max(0, self.elephant))

    def get_parts(self):
        return [self.bee, self.elephant]


be = BeeElephant(3, 2)
print(be.fly())
print(be.trumpet())
be.eat("grass", 4)
print(be.get_parts())

be = BeeElephant(13, 87)
print(be.fly())
print(be.trumpet())
be.eat("nectar", 90)
print(be.trumpet())
print(be.get_parts())
