import logging
import pytest
from api.account_api import AccountApi

url = "https://bookstore.toolsqa.com/"
header = {'accept': 'application/json'}
loginNone = {"userName": "temotddddooo", "password": "temOOOOOd£321@RRR"}
login = {"userName": "foo", "password": "tamdsar&ssD*DF123£"}
empty_user = {"userName": "", "password": ""}
new_user = {"userName": "adhhvyemd", "password": "ad£32h1FerDG&fff"}


@pytest.mark.failed
def test_post_login_account_not_found():
    """
    Try logging in with a non-existent account
    failed
    """
    logging.info("Try logging in with a non-existent account")
    response = AccountApi().post_login_authorized(loginNone)
    print(response)
    logging.info(f'Success login {response.status_code}')
    logging.warning(f'Error: Not Found , status code is: {response.status_code}')
    assert response.status_code == 200


@pytest.mark.passed
def test_post_login_account():
    """
    Check if the login with an existing account
    passed
    """
    logging.info("Check if the login with an existing account")
    response = AccountApi().post_login_authorized(login)
    print(response)
    logging.info(f'Success login {response.status_code}')
    logging.warning(f'Error: Not Found , status code is: {response.status_code}')
    assert response.status_code == 200


@pytest.mark.passed
def test_post_login_account_generate_token():
    """
    tries to get an authorized token for said account
    passed
    """
    logging.info("trying to get a token")
    response = AccountApi().post_login_account_generate_token(login)
    logging.warning(f"{response}")
    print(f'reeeeeeeeesss {response.status_code}')
    logging.info(f"successful registration, status code is : {response.status_code}")
    assert response.status_code == 200


@pytest.mark.failed
def test_post_login_account_generate_token_with_empty_usernameandpassword():
    """
    check post login account generate token with empty username and password
    failed
    """
    logging.info("send an empty password and empty username")
    response = AccountApi().post_login_account_generate_token(empty_user)
    logging.warning(f'Error: Not Found , status code is: {response.status_code}')
    assert response.status_code == 200


@pytest.mark.passed
def test_post_account_user():
    """
    Check if "Post Account User" has already posted or the user already exists
    passed
    """
    logging.info("Add new account user")
    response = AccountApi().post_account_user(new_user)
    logging.info(f'Successfully added a new user, status code is {response.status_code}')
    logging.warning(f'Error, User already exists, status code is {response.status_code}, add new user account')
    assert response.status_code == 201


@pytest.mark.passed
def test_post_account_user_empty():
    """
    Check if the account is empty Do not post
    passed
    """
    logging.info("Add an empty account user")
    response = AccountApi().post_account_user(empty_user)
    logging.info(f'Successfully added a new user, status code is {response.status_code}')
    logging.warning(f'Error: Bad Request, status code is {response.status_code}, add a new good account')
    assert response.status_code == 400


@pytest.mark.passed
def test_delete_user_non_existent():
    """
    Check to delete a non-existent account
    passed
    """
    logging.info("trying to delete a user with a 30 character userID")
    response = AccountApi().delete_user("f137ffc5-8809-41f9-b8f7-0b4ccf519436")
    logging.info(f'Successfully delete a user account, status code is {response.status_code}')
    logging.warning(f'Error, unsuccessful user account deletion, status code is {response.status_code}')
    assert response.status_code != 200


#geeeeeeeeeeeeeeeeeeeeetttt