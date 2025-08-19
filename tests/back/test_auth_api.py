from api.api_manager import ApiManager
from pydantic_models.user_model import RegisterUserResponse


class TestAuthAPI:

    # с использованием pydantic
    def test_register_user(self, api_manager: ApiManager, registration_user_data):
        response = api_manager.auth_api.register_user(user_data=registration_user_data, expected_status=(200, 201))
        register_user_response = RegisterUserResponse(**response.json())
        assert register_user_response.email == registration_user_data.email, "Email не совпадает"

    # Без pydantic
    def test_register_and_login_user(self, api_manager: ApiManager, registered_user, registration_user_data):
        login_data = {
            "email": registration_user_data.email,
            "password": registration_user_data.password
        }
        response = api_manager.auth_api.login_user(login_data)
        response_data = response.json()

        assert "accessToken" in response_data, "Токен доступа отсутствует в ответе"
        assert response_data["user"]["email"] == registration_user_data.email, "Email не совпадает"

    def test_super_admin(self, super_admin, common_user):
        print(super_admin.api.auth_api.session.headers)
