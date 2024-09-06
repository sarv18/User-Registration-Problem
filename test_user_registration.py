import pytest
from user_registration import UserRegistration

@pytest.mark.parametrize("first_name, expected", [
    ("Sarvesh", True),   # Valid case
    ("sarvesh", False),  # Invalid case: starts with a lowercase letter
    ("sar", False),      # Invalid case: too short
    ("sar4545", False),  # Invalid case: contains numbers
])
def test_users_first_name(first_name, expected):
    result = UserRegistration().users_first_name(first_name)
    assert result == expected

@pytest.mark.parametrize("last_name, expected", [
    ("Shelke", True),    # Valid case
    ("shelke", False),   # Invalid case: starts with a lowercase letter
    ("sh", False),       # Invalid case: too short
    ("sh123", False),    # Invalid case: contains numbers
])
def test_users_last_name(last_name, expected):
    result = UserRegistration().users_last_name(last_name)
    assert result == expected

@pytest.mark.parametrize("email, expected", [
    ("abc.xyz@bl.co.in", True),  # Valid case
    ("abc.xyz@bl.co", True),     # Valid case
    ("abc.xyz@bl", False),       # Invalid case: missing domain
    ("abc@bl.co", False),        # Invalid case: missing proper domain
])
def test_users_email(email, expected):
    result = UserRegistration().users_email(email)
    assert result == expected

@pytest.mark.parametrize("mobile, expected", [
    ("91 8766552550", True),     # Valid case
    ("8766552550", False),       # Invalid case: missing country code
    ("918766552550", False),     # Invalid case: no space after country code
])
def test_mobile_number(mobile, expected):
    result = UserRegistration().mobile_number(mobile)
    assert result == expected

@pytest.mark.parametrize("password, expected", [
    ("Sarvesh@01", True),        # Valid case
    ("8766552550@aA", True),     # Valid case
    ("8766552550", False),       # Invalid case: lacks special characters
    ("333344478@a", False),      # Invalid case: lacks uppercase letter
    ("hgwehfgjgkgew", False),    # Invalid case: lacks numbers and special characters
])
def test_password_rules(password, expected):
    result = UserRegistration().password_rules(password)
    assert result == expected
