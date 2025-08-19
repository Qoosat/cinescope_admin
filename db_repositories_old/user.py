from typing import Optional, List, Dict, Any
from db_repositories_old.base import BaseRepository
from db_models.user import User


class UserRepository(BaseRepository):
    """Репозиторий для работы с пользователями"""

    def get_user_by_id(self, user_id: str, db_name: str = "movies") -> Optional[User]:
        """Получение пользователя по ID"""
        with self.db_manager.get_session(db_name) as session:
            return session.query(User).filter(User.id == user_id).first()

    def get_users_by_email(self, email: str, db_name: str = "movies") -> List[User]:
        """Получение пользователей по email"""
        with self.db_manager.get_session(db_name) as session:
            return session.query(User).filter(User.email == email).all()

    def get_verified_users(self, db_name: str = "movies") -> List[User]:
        """Получение верифицированных пользователей"""
        with self.db_manager.get_session(db_name) as session:
            return session.query(User).filter(User.verified == True).all()

    def get_all_users(self, db_name: str = "movies") -> List[User]:
        """Получение всех пользователей"""
        with self.db_manager.get_session(db_name) as session:
            return session.query(User).all()

    def create_user(self, user_data: Dict[str, Any], db_name: str = "movies") -> User:
        """Создание пользователя"""
        with self.db_manager.get_session(db_name) as session:
            user = User(**user_data)
            session.add(user)
            session.flush()
            session.refresh(user)
            return user

    def update_user(self, user_id: str, update_data: Dict[str, Any], db_name: str = "movies") -> Optional[User]:
        """Обновление пользователя"""
        with self.db_manager.get_session(db_name) as session:
            user = session.query(User).filter(User.id == user_id).first()
            if user:
                for key, value in update_data.items():
                    setattr(user, key, value)
                session.flush()
                session.refresh(user)
                return user
            return None

    def delete_user(self, user_id: str, db_name: str = "movies") -> bool:
        """Удаление пользователя"""
        with self.db_manager.get_session(db_name) as session:
            user = session.query(User).filter(User.id == user_id).first()
            if user:
                session.delete(user)
                return True
            return False

