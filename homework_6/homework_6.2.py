def create_time_checker(max_time):
    def time_checker(test_time):
        if max_time >= test_time:
            print(f"Время теста: {test_time}, максимальное время не превышено.")
        else:
            raise ValueError("Превышено максимальное время.")

    return time_checker


try:
    time_check120 = create_time_checker(120)
    time_check120(60)
except ValueError as e:
    print(e)

try:
    time_check50 = create_time_checker(50)
    time_check50(60)
except ValueError as e:
    print(e)
