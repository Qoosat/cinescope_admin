from api.api_manager import ApiManager
import requests
import time


def test_helth_check():
    s = requests.session()
    a = ApiManager(s)

    num_requests = 100

    print("Запросы с использованием сессии:")
    start_time = time.time()
    try:
        for i in range(num_requests):
            login_data = {
                "email": "api1@gmail.com",
                "password": "asdqwe123Q"
            }
            a.auth_api.login_user(login_data)
    except Exception as e:
        print(f"ошибка: {e}")
    finally:
        a.close_session()  # закрываем сессию
        end_time = time.time()
        print(f"Время выполнения с сессией: {end_time - start_time:.4f} секунд\n")
