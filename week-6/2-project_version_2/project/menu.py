from display import print_skulls

class MenuItem:
    def __init__(self, firstletter, name, action):
        self.firstletter = firstletter.upper()
        self.name = name.upper()
        self.action = action

class Menu:
    def __init__(self, name, items, input_prompt):
        self.name = name.upper()
        self.items = items
        self.input_prompt = input_prompt

    def choose(self, firstletter):
        for item in self.items:
            if item.firstletter == firstletter:
                return item.action()

    def valid_inputs(self):
        valid_inputs = []
        for item in self.items:
            valid_inputs.append(item.firstletter)
        return valid_inputs

    def print_menu(self):
        print_skulls()
        print(" " + self.name + " ")
        print_skulls()
        for item in self.items:
            print(" " + item.firstletter + ": " + item.name + "\n")

    def store_selection(self):
        selection = input(self.input_prompt)
        return selection.upper()
