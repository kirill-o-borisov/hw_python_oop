import datetime as dt

class Calculator:

    def __init__(self, limit):  #Лимит кaлорий денег
        self.limit = limit
        self.records = []

    def add_record(self, rec):  # Добавляем запись
        self.records.append(rec)
            
    def get_today_stats(self):
        now = dt.date.today()
        total_amount = 0       
        for i in self.records:
            if i.date == now:
                total_amount += i.amount
        return total_amount
    
    def get_left(self):
        return (self.limit - self.get_today_stats())

    def get_week_stats(self):
        now = dt.date.today().date()
        seven_days_ago = now - dt.timedelta(days=7)
        total_amount_week = 0        
        for i in self.records:
            if i.date <= now and i.date > seven_days_ago:
                total_amount_week += i.amount
        return total_amount_week  # за неделю 
        
class CashCalculator(Calculator):
    
    def get_today_cash_remained(self, currency):
        USD_RATE = 75.00
        EURO_RATE = 90.00
        if currency == 'usd':
            money_left = round(self.get_left()/USD_RATE,2)
        elif currency == 'eur':
            money_left = round(self.get_left()/EURO_RATE,2)        
        if money_left > 0:
            return f'На сегодня осталось {money_left} {currency}'
        elif money_left == 0:
            return f'Денег нет, держись'
        else:
            return f'Денег нет, держись: твой долг {money_left} {currency}'


class CaloriesCalculator(Calculator):

    def get_today_calories_remained(self):
        colories_left = self.get_left()
        if colories_left > 0:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {colories_left} кКал '
        else:
            return f'Хватит есть!'
    

class Record:

    def __init__(self, amount, comment, date = None):  # amount сумма денег или калорий
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date,'%d.%m.%Y').date()
        


#r1 = Record(amount=145, comment='Безудержный шопинг', date='08.03.2019')
#r3 = Record(amount=691, comment='Катание на такси', date='08.03.2019')

calculator = CaloriesCalculator(1000)
calculator.add_record(Record(amount=300,
                                  comment='бар в Танин др',
                                  date='20.2.2021'))
print(calculator.get_today_calories_remained())

