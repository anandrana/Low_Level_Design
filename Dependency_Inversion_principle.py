# Bad Example
# class Keyboard:
#     def input(self):
#         return "Keystrokes"

# class Computer:
#     def __init__(self):
#         self.keyboard = Keyboard()

# Good Example
class IInputDevice:
    def input(self): pass

class Keyboard(IInputDevice):
    def input(self):
        return "Keystrokes"

class Computer:
    def __init__(self, input_device: IInputDevice):
        self.input_device = input_device

    def get_input(self):
        return self.input_device.input()

comp = Computer(Keyboard())
print(comp.get_input())
