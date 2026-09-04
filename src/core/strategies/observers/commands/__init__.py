from .exit_command import ExitCommand
from .model_command import ModelCommand
from .help_command import HelpCommand
from .status_command import StatusCommand
from .clear_command import ClearCommand
from .base_command import Command

class CommandRegistry:
    def __init__(self):
        self._commands = {}
        self._register_all_commands()
    
    def _register_all_commands(self):
        commands = [
            ExitCommand(),
            ModelCommand(),
            HelpCommand(),
            StatusCommand(),
            ClearCommand()
        ]
        for command in commands:
            self.register(command)
    
    def register(self, command: Command) -> None:
        self._commands[command.get_name()] = command
        for alias in command.get_aliases():
            self._commands[alias] = command
    
    def get_command(self, name: str):
        return self._commands.get(name.lower())
    
    def is_command(self, text: str) -> bool:
        return text.lower() in self._commands