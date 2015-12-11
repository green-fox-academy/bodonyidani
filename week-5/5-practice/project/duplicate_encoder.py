class EncodeString():
    def __init__(self, string):
        self.string = string.lower()

    def encode_character(self, character):
        return "(" if self.string.count(character) == 1 else ")"

    def encode(self):
        output = ""
        for character in self.string:
            output += self.encode_character(character)
