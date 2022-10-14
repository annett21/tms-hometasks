class Talking:
    def __init__(self, name):
        self.name = name
        self.answer = True
        self.yes = 0
        self.no = 0

    def to_answer(self):
        if self.answer:
            self.answer = False
            self.yes += 1
            return "moore-moore"
        else:
            self.answer = True
            self.no += 1
            return "meow-meow"

    def number_yes(self):
        return self.yes

    def number_no(self):
        return self.no


tk = Talking("Pussy")
print(tk.to_answer())
print(tk.to_answer())
print(tk.to_answer())
print(
    f"{tk.name} says 'yes' {tk.number_yes()} times,"
    f"'no' {tk.number_no()} times"
)
tk = Talking("Pussy")
tk2 = Talking("Barsik")
print(tk.to_answer())
print(tk2.to_answer())
print(tk2.to_answer())
print(tk2.to_answer())
print(
    f"{tk.name} says 'yes' {tk.number_yes()} times,"
    f"'no' {tk.number_no()} times"
)
print(
    f"{tk2.name} says 'yes' {tk2.number_yes()} times,"
    f"'no' {tk2.number_no()} times"
)
