def get_message():
    """Return the application welcome message."""
    return "Hello from DVP Week 12 CI/CD Pipeline!"


def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


if __name__ == "__main__":
    print(get_message())
    print(f"2 + 3 = {add_numbers(2, 3)}")
