from typing import Optional, List, Dict, Any
from sqlalchemy import text
from config.database import DatabaseManager


class BaseRepository:
    """Базовый репозиторий с универсальным SQL методом"""

    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager

    def execute_sql(self, query: str, params: Dict[str, Any] = None, db_name: str = "movies") -> List[Dict]:
        """Универсальный метод для выполнения SQL запросов"""
        with self.db_manager.get_engine(db_name).connect() as connection:
            result = connection.execute(text(query), params or {})
            return [dict(row._mapping) for row in result.fetchall()]

    def execute_sql_single(self, query: str, params: Dict[str, Any] = None, db_name: str = "movies") -> Optional[Dict]:
        """Выполнение SQL запроса с ожиданием одной записи"""
        results = self.execute_sql(query, params, db_name)
        return results[0] if results else None
