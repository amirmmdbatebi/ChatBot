from abc import ABC, abstractmethod


class DocumentConverter(ABC):
    @abstractmethod
    def convert(self, file_path: str) -> str:
        """Read the file at the given path and return its content as Markdown."""