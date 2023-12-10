from datetime import datetime, timedelta

def main():
    print(
        f"Сегодня {datetime.today().date()} "
        f"День недели - 4 "
    )
    n = int(input("Введите количество дней: "))
    today = datetime.today()
    result = today + timedelta(days=n)
    print(
        f"Через {n} дней будет {result.date()} "
        f"День недели - {result.isoweekday()} "
    )

if __name__ == "__main__":
    main()