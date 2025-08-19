from pathlib import Path
from datetime import datetime


class Tools:
    @staticmethod
    def project_dir():
        """
        Возвращает корневую директорию проекта
        """
        return Path(__file__).parent.parent

    @staticmethod
    def files_dir(nested_directory: str = None,  filename: str = None):
        """
        Возвращает путь к директории `files` (или её поддиректории).
        Если директория не существует, она создается
        Если указан `filename`, возвращает полный путь к файлу
        """
        files_path = Tools.project_dir() / "files"
        if nested_directory:
            files_path = files_path / nested_directory
        files_path.mkdir(parents=True, exist_ok=True)

        if filename:
            return files_path / filename
        return files_path

    @staticmethod
    def get_timestamp():
        return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
