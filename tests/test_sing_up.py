import pytest
from .test_data import generate_random_email, invalid_emails
random_email = generate_random_email()

@pytest.mark.parametrize("first_name, last_name, email, password, confirm_password, empty_field, expected_error", [
    ("", "Tester", random_email, "Qwe123456@", "Qwe123456@", "first_name_error", "This is a required field."),
    ("Tester", "", random_email, "Qwe123456@", "Qwe123456@", "last_name_error", "This is a required field."),
    ("Tester", "Tester", "", "Qwe123456@", "Qwe123456@", "email_error", "This is a required field."),
    ("Tester", "Tester", random_email, "", "Qwe123456@", "password_error", "This is a required field."),
    ("Tester", "Tester", random_email, "Qwe123456@", "", "confirm_password_error", "This is a required field.")
])
def test_all_fields_are_required(home_page, sign_up_page, first_name, last_name, email, password, confirm_password, empty_field, expected_error):
    home_page.open_sign_up_form()
    sign_up_page.sign_up(first_name, last_name, email, password, confirm_password)
    errors = sign_up_page.get_required_field_error()
    actual_error = errors[empty_field]
    assert actual_error == expected_error, f"Expected error '{expected_error}' but got '{actual_error}'."


def test_valid_sign_up(home_page, sign_up_page, cabinet_page):
    home_page.open_sign_up_form()
    sign_up_page.sign_up("Tester", "Tester", random_email, "Qwe123456@", "Qwe123456@")
    actual_title = cabinet_page.get_page_title()
    assert actual_title == "My Account", f"The page title does not match 'My Account'. Actual title: '{actual_title}'"


@pytest.mark.parametrize("invalid_email", invalid_emails)
def test_error_displays_if_enter_invalid_email(home_page, sign_up_page, invalid_email):
    home_page.open_sign_up_form()
    sign_up_page.sign_up("Tester", "Tester", invalid_email, "Qwe123456@", "Qwe123456@")
    actual_error_message = sign_up_page.get_invalid_email_error_text()
    assert actual_error_message == "Please enter a valid email address (Ex: johndoe@domain.com).", \
                                   f"Error message is not displayed. Actual message: '{actual_error_message}'"


