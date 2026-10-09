def retry(count):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(count):
                print(f"Попытка №{i + 1}")
                result = func(*args, **kwargs)
                if result is True:
                    break
            return f"Количество попыток: {i + 1}"

        return wrapper

    return decorator


@retry(10)
def limit_chek(time):
    if time[0] >= 60:
        print(f"Время: {time[0]}")
        return True
    else:
        print(f"Время: {time[0]}")
        time[0] += 1
        return False


print(limit_chek([55]))
