from functools import wraps

def log_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Имя функции: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Функция завершила выполнение с результатом - {result}")
        return result
    return wrapper


def create_time_checker(max_time):

    @log_test
    def time_checker(test_time):
        """Функция проверки времени выполнения"""
        if max_time >= test_time:
            print(f"Время теста: {test_time}, максимальное время не превышено.")
            return "Success"
        else:
            return "Превышено максимальное время."

    return time_checker

time_check120 = create_time_checker(120)
time_check120(60)
print(f"\nНазвание функции: {time_check120.__name__},\nОписание функции: {time_check120.__doc__}")