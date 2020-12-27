import datetime as dt
class Record:
    def __init__(self, amount, comment, date = dt.datetime.now()):
        self.amount = amount
        self.comment = comment
        if isinstance(date, str):
            self.date = (dt.datetime.strptime(date, "%d.%m.%Y").date())
        else:
            self.date = date.date()  
class Calculator:
    records = []
    def __init__(self, limit):
        self.limit = limit
    def add_record(self, Record):
        self.records.append([Record.amount, Record.comment, Record.date])
    def get_today(self):
        today_stats = 0
        for record in self.records:
            if record[2] == dt.datetime.now().date():
                today_stats += record[0]
        return today_stats
    def get_today_remained(self):
        for record in self.records:
            if record[2] == dt.datetime.now().date():
                self.limit -= record[0]
        return self.limit
    def get_week(self):
        week_stats = 0
        for record in self.records:
            if record[2]>=(dt.datetime.now() - dt.timedelta(days=7)).date():
                week_stats += record[0]
        return week_stats
class CaloriesCalculator(Calculator):
    def add_record(self, Record):
        Calculator.add_record(self, Record)
    def get_today_stats(self):
        return Calculator.get_today(self)
    def get_calories_remained(self, currency):
        self.currency = currency
        Calculator.get_today_remained(self)
        self.currency = "кКал"
        if self.limit > 0:
            balance = (f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более  {round(self.limit)} {self.currency}")
        elif self.limit == 0:
            balance = (f"Хватит есть!")
        else:
            balance = (f"Хватит есть! {round(abs(self.limit))} {self.currency}")
        return balance
    def get_week_stats(self):
        return Calculator.get_week(self)
# заполняем лимит калорий
Calc = CaloriesCalculator(1000)
# сколько съели сегодня в r1
r1 = Record(amount=1200, comment="Ели много")
r2 = Record(amount=800, comment="В норме", date="26.12.2020")
r3 = Record(amount=700, comment="Баночка чипсов", date="25.12.2020")
r4 = Record(amount=433, comment="Винишко", date="24.12.2020")
r5 = Record(amount=500, comment="Кусок тортика. И ещё один.", date="23.12.2020")
r6 = Record(amount=1200, comment="В мак больше не ходим", date="22.12.2020")
r7 = Record(amount=1000, comment="Йогурт", date="21.12.2020")
Calc.add_record(r1)
Calc.add_record(r2)
Calc.add_record(r3)
Calc.add_record(r4)
Calc.add_record(r5)
Calc.add_record(r6)
Calc.add_record(r7)
print(Calc.get_today_stats())
print(Calc.get_calories_remained("кКал"))
print(Calc.get_week_stats())