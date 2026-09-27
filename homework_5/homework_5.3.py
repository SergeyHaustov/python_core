def test_info(count, timeout):
    if not 0 <= count <= 5:
        raise ValueError("Количество запусков должно быть в диапазоне от 0 до 5.\n")
    elif timeout <= 0:
        raise ValueError("Таймаут не может быть отрицательным.\n")
    else:
        print(f"Количество запусков: {count}\n"
              f"Таймаут: {timeout}\n")


try:
    test_info(5, 10)
except ValueError as e:
    print(e)

try:
    test_info(10, 50)
except ValueError as e:
    print(e)

try:
    test_info(5, -10)
except ValueError as e:
    print(e)
