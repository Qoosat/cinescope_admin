from pydantic_models.user_model import TestUser
from venv import logger
import json


def test_registered_user(registration_user_data, creation_user_data):
    user = TestUser(**registration_user_data)
    logger.info(user)

    user1 = TestUser(**creation_user_data)
    # logger.info(user1)

    json_data = user.model_dump_json(exclude_unset=True)
    logger.info(json_data)

    user2 = TestUser.model_validate_json(json_data)
    logger.info(user2)


def test_fixture_data(booking_data):
    print(booking_data)
    a = booking_data()
    print(f'\n booking_data#1 \n',a)
    b = booking_data()
    print(f'\n booking_data#2 \n', b)

