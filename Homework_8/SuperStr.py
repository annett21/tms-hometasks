class SuperStr(str):
    def is_repeatance(self, s):
        if not self or not s or not isinstance(s, str):
            return False
        return self.lower() == s.lower() * (len(self) // len(s))

    def is_palindrome(self):
        return self.lower() == self.lower()[::-1]


text = SuperStr("madam")
print(text.is_repeatance("Madam"))
print(f"Is {text} a palindrome?", text.is_palindrome())
