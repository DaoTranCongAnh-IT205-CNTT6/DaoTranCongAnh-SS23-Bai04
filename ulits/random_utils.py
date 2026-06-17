import random
import string


def generate_assignment_code():

    characters = (
        string.ascii_uppercase +
        string.digits
    )

    random_part = "".join(
        random.choice(characters)
        for _ in range(4)
    )

    return f"PY-{random_part}"