from .base import DocumentConverter
import pymupdf4llm

class PdfConverter(DocumentConverter):
    def convert(self, file_path: str) -> str:
        return pymupdf4llm.to_markdown(file_path)