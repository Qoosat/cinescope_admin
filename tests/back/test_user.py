from pydantic_models.user_model import RegisterUserResponse


class TestUser:

    # C pydantic
    def test_create_user(self, super_admin, creation_user_data):
        response = super_admin.api.user_api.create_user(creation_user_data.model_dump(mode='json')).json()
        register_user_response = RegisterUserResponse(**response)

        assert register_user_response.email == creation_user_data.email
        assert register_user_response.fullName == creation_user_data.fullName
        assert register_user_response.roles == creation_user_data.roles
        assert register_user_response.verified == creation_user_data.verified
        # assert register_user_response.banned == creation_user_data.banned

    # Без pydantic (не будет работать)
    def test_get_user_by_locator(self, super_admin, creation_user_data):
        created_user_response = super_admin.api.user_api.create_user(creation_user_data).json()
        response_by_id = super_admin.api.user_api.get_user(created_user_response['id']).json()
        response_by_email = super_admin.api.user_api.get_user(creation_user_data['email']).json()

        assert response_by_id == response_by_email, "Содержание ответов должно быть идентичным"
        assert response_by_id.get('id') and response_by_id['id'] != '', "ID должен быть не пустым"
        assert response_by_id.get('email') == creation_user_data['email']
        assert response_by_id.get('fullName') == creation_user_data['fullName']
        assert response_by_id.get('roles', []) == creation_user_data['roles']
        assert response_by_id.get('verified') is True

    # Без pydantic (не будет работать)
    def test_get_user_by_id_common_user(self, common_user, super_admin, api_manager):
        api_manager.user_api.get_user(common_user.email, expected_status=401)
        common_user.api.user_api.get_user(common_user.email, expected_status=403)
        super_admin.api.user_api.get_user(common_user.email, expected_status=201)


    """
    Пример параметризации с использованием фикстур в качестве параметров
    """
    import pytest

    @pytest.fixture
    def user(self, request):
        return request.getfixturevalue(request.param)

    @pytest.mark.parametrize('user,expected_code', [('super_admin', 200), ('common_user', 403)], indirect=['user'])
    def test_users(self, user, common_user, expected_code):
        user.api.user_api.get_user(common_user.email, expected_status=expected_code)
