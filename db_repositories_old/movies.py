from typing import Optional, List, Dict, Any
from db_repositories_old.base import BaseRepository
from db_models.movies import Movies


class MoviesRepository(BaseRepository):
    """Репозиторий для работы с фильмами"""

    def get_movie_by_id(self, movie_id: str, db_name: str = "movies") -> Optional[Movies]:
        """Получение фильма по ID"""
        with self.db_manager.get_session(db_name) as session:
            return session.query(Movies).filter(Movies.id == movie_id).first()

    def get_movies_by_year(self, year: int, db_name: str = "movies") -> List[Movies]:
        """Получение фильмов по году"""
        with self.db_manager.get_session(db_name) as session:
            return session.query(Movies).filter(Movies.year == year).order_by(Movies.rating.desc()).all()

    def get_movies_by_director(self, director: str, db_name: str = "movies") -> List[Movies]:
        """Поиск фильмов по режиссеру"""
        with self.db_manager.get_session(db_name) as session:
            return session.query(Movies).filter(Movies.director.ilike(f"%{director}%")).order_by(Movies.year.desc()).all()

    def get_top_rated_movies(self, limit: int = 10, db_name: str = "movies") -> List[Movies]:
        """Получение топ фильмов по рейтингу"""
        with self.db_manager.get_session(db_name) as session:
            return session.query(Movies).order_by(Movies.rating.desc()).limit(limit).all()

    def get_movies_by_genre(self, genre: str, db_name: str = "movies") -> List[Movies]:
        """Получение фильмов по жанру"""
        with self.db_manager.get_session(db_name) as session:
            return session.query(Movies).filter(Movies.genre.ilike(f"%{genre}%")).all()

    def get_all_movies(self, db_name: str = "movies") -> List[Movies]:
        """Получение всех фильмов"""
        with self.db_manager.get_session(db_name) as session:
            return session.query(Movies).all()

    def create_movie(self, movie_data: Dict[str, Any], db_name: str = "movies") -> Movies:
        """Создание фильма"""
        with self.db_manager.get_session(db_name) as session:
            movie = Movies(**movie_data)
            session.add(movie)
            session.flush()
            session.refresh(movie)
            return movie

    def update_movie(self, movie_id: str, update_data: Dict[str, Any], db_name: str = "movies") -> Optional[Movies]:
        """Обновление фильма"""
        with self.db_manager.get_session(db_name) as session:
            movie = session.query(Movies).filter(Movies.id == movie_id).first()
            if movie:
                for key, value in update_data.items():
                    setattr(movie, key, value)
                session.flush()
                session.refresh(movie)
                return movie
            return None

    def delete_movie(self, movie_id: str, db_name: str = "movies") -> bool:
        """Удаление фильма"""
        with self.db_manager.get_session(db_name) as session:
            movie = session.query(Movies).filter(Movies.id == movie_id).first()
            if movie:
                session.delete(movie)
                return True
            return False
