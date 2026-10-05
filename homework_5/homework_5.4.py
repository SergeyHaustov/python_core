class InvalidTestStatusError(Exception):
    """Некорректный статус теста"""
    pass


def test_status(status):
    if status not in ["PASS", "FAIL", "SKIP"]:
        raise InvalidTestStatusError(f"Некорректный статус: {status}")
    print("Статус принят.")


try:
    status1 = input("Введите статус: ").upper()
    test_status(status1)
except InvalidTestStatusError as e:
    print(e)
