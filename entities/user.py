from api.api_manager import ApiManager


class User:
    def __init__(self, email: str, password: str, roles: list, api: ApiManager):
        self.email = email
        self.password = password
        self.roles = roles
        self.api = api  # Экземпляр API Manager для запросов

    @property
    def creds(self):
        """Возвращает кортеж (email, password)"""
        return self.email, self.password


if __name__ == "__main__":
    a1 = object()
    User("bhjfd@fdij.ru", '123123', roles="es", api=a1)
