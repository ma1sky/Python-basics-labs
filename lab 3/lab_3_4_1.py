from datetime import datetime

def nearest_date(*dates: list) -> str:
    now = datetime.today().date()
    closeDate = min(dates, key = lambda x: abs(datetime.strptime(x, '%d.%m.%Y').date() - now))
    return closeDate


print(nearest_date("10.10.2020", "10.10.2022", "10.10.2024"))