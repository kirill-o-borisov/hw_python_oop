import datetime as dt


class Calculator:

    def __init__(self, limit):  # Лимит кaлорий денег
        self.limit = limit
        self.records = []

    def add_record(self, rec):  # Добавляем запись
        self.records.append(rec)

    def get_today_stats(self):  # Вывод за день
        now = dt.date.today()
        total_amount = 0
        for i in self.records:
            if i.date == now:
                total_amount += i.amount
        return total_amount

    def get_left(self):  # Получение остатка
        return (self.limit - self.get_today_stats())

    def get_week_stats(self):
        now = dt.date.today().date()
        seven_days_ago = now - dt.timedelta(days=7)
        total_amount_week = 0
        for i in self.records:
            if i.date <= now and i.date > seven_days_ago:
                total_amount_week += i.amount
        return total_amount_week  # За неделю


class CashCalculator(Calculator):
    USD_RATE = 75.00
    EURO_RATE = 90.00

    def get_today_cash_remained(self, currency):
        if currency == 'usd':
            money_left = round(self.get_left() / self.USD_RATE, 2)
        elif currency == 'eur':
            money_left = round(self.get_left() / self.EURO_RATE, 2)
        if money_left > 0:
            return f'На сегодня осталось {money_left} {currency}'
        elif money_left == 0:
            return 'Денег нет, держись'
        else:
            return f'Денег нет, держись: твой долг {money_left} {currency}'


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        colories_left = self.get_left()
        if colories_left > 0:
            return (f'Сегодня можно съесть что-нибудь ещё, '
                    f'но с общей калорийностью не более {colories_left} кКал')
        else:
            return 'Хватит есть!'


class Record:

    def __init__(self, amount, comment, date=None):  # Тут amount сумма
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
