class Themes(list):
    def __init__(self, themes):
        self.themes = themes

    def add_theme(self, value):
        self.themes.append(value)

    def shift_one(self):
        last_elem = self.themes.pop(-1)
        self.themes.insert(0, last_elem)

    def reverse_order(self):
        self.themes.reverse()

    def get_themes(self):
        return self.themes

    def get_first(self):
        return self.themes[0]


t1 = Themes(["weather", "rain"])
t1.add_theme("warm")
print(t1.get_themes())
t1.shift_one()
print(t1.get_first())

t2 = Themes(["sun", "feeding"])
t2.add_theme("cool")
t2.shift_one()
print(t2.get_first())
t2.reverse_order()
print(t2.get_themes())
