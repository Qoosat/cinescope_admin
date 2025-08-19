import requests

from api.auth_api import AuthApi
from api.user_api import UserApi
from api.movies_api import MoviesApi


class ApiManager:
    """
    Класс для управления API-классами с единой HTTP-сессией.
    """
    def __init__(self, session):
        """
        Инициализация ApiManager.
        :param session: HTTP-сессия, используемая всеми API-классами.
        """
        self.session = session
        self.auth_api = AuthApi(session)
        self.movies_api = MoviesApi(session)
        self.user_api = UserApi(session)

    def close_session(self):
        self.session.close()


if __name__ == "__main__":
    s = requests.session()
    a = ApiManager(s)
    r = a.movies_api.get_movies()
    print(r)
