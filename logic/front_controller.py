from userinterface.user_interface import UserInterface
from logic.command_interpreter import CommandInterpreter
from logic.logic_add import AddLogic
from logic.logic_create import CreateLogic
from logic.logic_select import SelectLogic

class FrontController:
    def __init__(self):
        self.ui = UserInterface()
        self.ci = CommandInterpreter()
        self.ui.say_hello()
        self.logic_dictionary = {'create': CreateLogic, 'add': AddLogic, 'select': SelectLogic}

    def run(self):
        while True:
            command = self.ui.user_input()
            command_dictionary = self.ci.interpreter(command)
            self.logic_dictionary[command_dictionary.get('command_name')](command_dictionary.get('document_name'), 
            command_dictionary.get('columns'), command_dictionary.get('values'))
