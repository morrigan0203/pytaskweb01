import pytest
from gb import auth


@pytest.fixture()
def incorrect_word():
    return "babt"


@pytest.fixture()
def correct_word():
    return "baby"


@pytest.fixture()
def authorization():
    return auth()


@pytest.fixture()
def found_title():
    return "sdfsdf"


@pytest.fixture()
def new_title():
    return "new_title"

