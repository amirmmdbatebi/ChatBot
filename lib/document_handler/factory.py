import os

from .base import DocumentConverter
from .docx import DocxConverter
from .pdf import PdfConverter


def get_converter(file_path: str) -> DocumentConverter:
    extension = os.path.splitext(file_path)[1].lower()
    if extension == ".pdf":
        return PdfConverter()
    if extension == ".docx":
        return DocxConverter()
    raise ValueError(f"Unsupported file type: {extension}")