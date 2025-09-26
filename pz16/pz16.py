class Calendar:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def is_leap_year(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

    def days_in_month(self):
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.month in [4, 6, 9, 11]:
            return 30
        elif self.month == 2:
            return 29 if self.is_leap_year() else 28
        else:
            raise ValueError("Некорректный меся")

    def day_of_week(self):
        q = self.day
        m = self.month
        year = self.year
        
        if m < 3:
            m += 12
            year -= 1
            
        K = year % 100
        J = year // 100
        f = q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) - (2 * J)
        return f % 7

calendar = Calendar(2023, 10, 5)
print("Високосный год:", calendar.is_leap_year())
print("Количество дней в месяце:", calendar.days_in_month())
print("День недели:", calendar.day_of_week())
