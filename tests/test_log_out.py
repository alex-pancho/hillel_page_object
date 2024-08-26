import pytest

def test_log_out(log_out_page):
    log_out_page.log_out()
    assert log_out_page.item("guest_btn").is_visible(), "Logout failed: Guest button is not visible."
