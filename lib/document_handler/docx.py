from .base import DocumentConverter
import mammoth


class DocxConverter(DocumentConverter):
    def convert(self, file_path: str) -> str:
        with open(file_path, "rb") as file:
            result = mammoth.convert_to_markdown(file)
        return result.value