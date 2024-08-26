import pytest

@pytest.mark.parametrize("first_name, last_name, email, password, confirm_password", [
    ("Karyn", "Tashchi", "karyn.tashchi@example.com", "Password123!", "Password123!")
])
def test_successful_sign_up(sign_up_page, first_name, last_name, email, password, confirm_password):
    sign_up_page.open_sign_up_form()  # Спочатку відкриваємо форму реєстрації
    sign_up_page.fill_form(first_name, last_name, email, password, confirm_password)
    # Перевіряємо, що форма закрилася після успішної реєстрації
    assert sign_up_page.is_form_closed(), "Sign-up failed: The form did not close as expected."
