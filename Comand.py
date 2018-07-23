#Command pattern

class Command():
    #abstract class
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        #abstract method
        pass

class ConcreteCommand(Command):
    #Concrete command
    def execute(self):
        self.receiver.action()

class Receiver:
    def action(self):
        print("Action is performing here")

class Invoker:
    def __init__(self):
        self.commands = list()

    def store_command(self, command):
        self.commands.append(command)

    def execute_commands(self):
        for command in self.commands:
            command.execute()

def main():
    receiver = Receiver()
    concrete_command = ConcreteCommand(receiver)
    invoker = Invoker()
    invoker.store_command(concrete_command)
    invoker.execute_commands()

if __name__ == "__main__":
    main()

    #OUTPUT:
    #Action is performing here