import json
import os
from datetime import datetime
from typing import List, Dict
from .base_observer import ChatObserver
from core.chat_status import ChatStatus

class FileLoggerObserver(ChatObserver):
    def __init__(self, file_path: str = "logs/chat_logs.json"):
        self.file_path = file_path
        self._ensure_directory_exists()
        self._initialize_file()
    
    def _ensure_directory_exists(self) -> None:
        directory = os.path.dirname(self.file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
    
    def _initialize_file(self) -> None:
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump([], f, ensure_ascii=False, indent=2)
    
    def _load_logs(self) -> List[Dict]:
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    
    def _save_logs(self, logs: List[Dict]) -> None:
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(logs, f, ensure_ascii=False, indent=2)
    
    def on_message_received(self, user_message: str, bot_response: str) -> None:
        logs = self._load_logs()
        logs.append({
            "timestamp": datetime.now().isoformat(),
            "type": "message",
            "user_message": user_message,
            "bot_response": bot_response
        })
        self._save_logs(logs)
    
    def on_error(self, error_message: str) -> None:
        logs = self._load_logs()
        logs.append({
            "timestamp": datetime.now().isoformat(),
            "type": "error",
            "error_message": error_message
        })
        self._save_logs(logs)
    
    def on_status_change(self, status: ChatStatus) -> None:
        logs = self._load_logs()
        logs.append({
            "timestamp": datetime.now().isoformat(),
            "type": "status_change",
            "status": status.name,
            "status_description": status.get_description()
        })
        self._save_logs(logs)