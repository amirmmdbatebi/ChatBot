from typing import List, Dict, Optional
from .event_dispatcher import EventDispatcher
from .chat_status import ChatStatus
from .config import AppConfig
from .exceptions import InvalidInputError, StrategyError
from strategies.base_strategy import LLMStrategy
from observers.base_observer import ChatObserver


class ChatBot:
    def __init__(
        self,
        strategy: LLMStrategy,
        config: Optional[AppConfig] = None,
        observers: Optional[List[ChatObserver]] = None
    ):
        self._strategy = strategy
        self._config = config or AppConfig()
        self._event_dispatcher = EventDispatcher()
        self._conversation_history: List[Dict[str, str]] = []
        self._status = ChatStatus.IDLE
        
        self._initialize_conversation()
        
        if observers:
            for observer in observers:
                self.attach_observer(observer)
        
        self._config.validate()
    
    def _initialize_conversation(self) -> None:
        self._conversation_history = [
            {"role": "system", "content": self._config.system_prompt}
        ]
    
    def send_message(self, user_message: str) -> str:
        if not user_message or not user_message.strip():
            raise InvalidInputError("پیام نمی‌تواند خالی باشد")
        
        self._set_status(ChatStatus.PROCESSING)
        
        try:
            self._add_to_history("user", user_message.strip())
            
            response = self._strategy.generate_response(
                messages=self._conversation_history,
                temperature=self._config.chat_temperature
            )
            
            self._add_to_history("assistant", response)
            self._event_dispatcher.notify_message(user_message.strip(), response)
            self._set_status(ChatStatus.IDLE)
            
            return response
            
        except Exception as e:
            self._rollback_last_message()
            self._event_dispatcher.notify_error(str(e))
            self._set_status(ChatStatus.IDLE)
            raise StrategyError(f"خطا در تولید پاسخ: {e}")
    
    def set_strategy(self, strategy: LLMStrategy) -> None:
        self._strategy = strategy
        self._initialize_conversation()
        self._set_status(ChatStatus.IDLE)
        print(f"\n🔄 استراتژی به '{strategy.get_name()}' تغییر یافت")
    
    def set_model(self, model_name: str) -> None:
        self._strategy.set_model(model_name)
        self._initialize_conversation()
        self._set_status(ChatStatus.IDLE)
    
    def attach_observer(self, observer: ChatObserver) -> None:
        self._event_dispatcher.attach(observer)
        observer.on_status_change(self._status)
    
    def detach_observer(self, observer: ChatObserver) -> None:
        self._event_dispatcher.detach(observer)
    
    def get_observer_count(self) -> int:
        return self._event_dispatcher.get_observer_count()
    
    def _set_status(self, status: ChatStatus) -> None:
        if self._status != status:
            self._status = status
            self._event_dispatcher.notify_status_change(status)
    
    def _add_to_history(self, role: str, content: str) -> None:
        self._conversation_history.append({"role": role, "content": content})
        
        if len(self._conversation_history) > self._config.max_history_length:
            self._conversation_history = [
                self._conversation_history[0]
            ] + self._conversation_history[-(self._config.max_history_length - 1):]
    
    def _rollback_last_message(self) -> None:
        if len(self._conversation_history) > 1:
            self._conversation_history.pop()
    
    def get_history(self) -> List[Dict[str, str]]:
        return self._conversation_history.copy()
    
    def clear_history(self) -> None:
        self._initialize_conversation()
        self._set_status(ChatStatus.IDLE)
    
    def get_strategy_name(self) -> str:
        return self._strategy.get_name()
    
    def get_available_models(self) -> List[str]:
        return self._strategy.get_available_models()
    
    def get_current_model(self) -> str:
        return self._strategy.get_current_model()
    
    def get_status(self) -> ChatStatus:
        return self._status