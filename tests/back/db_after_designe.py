"""
Тесты для работы с фильмами
"""
import datetime
from pytz import timezone
from sqlalchemy.orm import Session
from database.db_helpers import DBHelper


class TestMovies:
    """Класс тестов для фильмов"""

    def test_db_requests(self, super_admin, db_helper, created_test_user):
        assert created_test_user == db_helper.get_user_by_id(created_test_user.id)
        assert db_helper.user_exists_by_email("api1@gmail.com")




    def test_movie_creation_with_validation(self, db_session: Session):
        """Тест создания фильма с валидацией данных"""

        # Создаем данные фильма
        movie_data = DataGenerator.generate_movie_data()

        # Создаем фильм
        movie = DBHelper.create_test_movie(db_session, movie_data)

        try:
            # Проверяем что все поля заполнены корректно
            assert movie.id == movie_data["id"]
            assert movie.name == movie_data["name"]
            assert movie.price == movie_data["price"]
            assert movie.published == movie_data["published"]

            # Проверяем что фильм существует в базе
            assert DBHelper.movie_exists_by_name(db_session, movie.name)

        finally:
            # Cleanup - удаляем тестовые данные
            DBHelper.delete_movie(db_session, movie)

    def test_get_movie_by_various_fields(self, db_session: Session):
        """Тест получения фильма по различным полям"""

        # Создаем тестовый фильм
        movie_data = DataGenerator.generate_movie_data()
        created_movie = DBHelper.create_test_movie(db_session, movie_data)

        try:
            # Получаем по ID
            movie_by_id = DBHelper.get_movie_by_id(db_session, created_movie.id)
            assert movie_by_id is not None
            assert movie_by_id.id == created_movie.id

            # Получаем по названию
            movie_by_name = DBHelper.get_movie_by_name(db_session, created_movie.name)
            assert movie_by_name is not None
            assert movie_by_name.name == created_movie.name

        finally:
            # Cleanup
            DBHelper.delete_movie(db_session, created_movie)