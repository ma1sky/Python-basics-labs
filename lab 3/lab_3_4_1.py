from datetime import datetime

def nearest_date(*dates: list) -> str:
    now = datetime.today().date()
    closeDate = min(dates, key = lambda x: abs(datetime.strptime(x, '%d.%m.%Y').date() - now))
    return closeDate

while True:
    try:
        print(nearest_date(*list(str(date) for date in input().split())))
    except ValueError:
        print('Введен неверный формат входных данных')