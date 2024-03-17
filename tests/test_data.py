import uuid


def generate_random_email():
    return f"test_{uuid.uuid4()}@example.com"


invalid_emails = [
    "plainaddress",
    "@missingusername.com",
    "Joe Smith <email@domain.com>",
    "email.domain.com",
    "email@domain@domain.com",
    ".email@domain.com",
    "email.@domain.com",
    "email..email@domain.com",
    "email@domain.com (Joe Smith)",
    "email@domain",
    "email@-domain.com",
    "email@domain..com"
]
