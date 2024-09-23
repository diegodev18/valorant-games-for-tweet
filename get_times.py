from datetime import datetime


def get_sleep_time(day=datetime.now().day, hour=0, minute=0, second=0, microsecond=0):
    now = datetime.now().replace(microsecond=microsecond)
    now_target = now.replace(day=day, hour=hour, minute=minute, second=second, microsecond=microsecond)
    return (now_target - now).total_seconds()


if __name__ == '__main__':
    print(get_sleep_time(day=datetime.now().day + 1), get_sleep_time(hour=15))