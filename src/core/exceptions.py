class ChatBotError(Exception):
    pass

class StrategyError(ChatBotError):
    pass

class ObserverError(ChatBotError):
    pass

class ConfigurationError(ChatBotError):
    pass

class AuthenticationError(StrategyError):
    pass

class RateLimitError(StrategyError):
    pass

class ModelNotFoundError(StrategyError):
    pass

class InvalidInputError(ChatBotError):
    pass