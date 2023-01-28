
import pytest

from things_to_test import search_in_file, add_from_json, Storage


@pytest.fixture
def pytest_function1():
    result = search_in_file('unittest_file.txt', 'EAT')
    assert result == ['EAT\n']

def test_search_in_file_positive(pytest_function1):
    return search_in_file('unittest_file.txt', 'EAT')

@pytest.fixture
def pytest_function2():
    result = add_from_json('json_file_for_unittest', {"a": 3, "b": 4})
    assert result == 7

def test_add_from_json_positive(pytest_function2):
    return add_from_json('json_file_for_unittest', {"a": 3, "b": 4})


@pytest.fixture(scope='module')

def pytest_classStorage():
    return {}

def test_classStorage(pytest_classStorage):
    pytest_classStorage = {}
    return pytest_classStorage




