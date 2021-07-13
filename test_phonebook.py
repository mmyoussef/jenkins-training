import sys
import pytest
sys.path.append(".")
from phonebook import PhoneBook

@pytest.fixture
def phonebook():
    return PhoneBook()

def test_phone_lookup(phonebook):
    phonebook.add('bob','12345')
    number = phonebook.lookup('bob')
    assert '1345' == number


def test_missing_name():
    phonebook.add("name","123456")
    with pytest.raises(KeyError):
        phonebook.lookup("name")
