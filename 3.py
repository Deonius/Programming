class Employee:
    def calculate_payroll(self):
        pass

class hourlyemployee(Employee):
    def __init__(self,hours):
        self.hours=hours
    def calculate_payroll(self):
        self.pay = 20.8*8*self.hours
    def print_info(self):
        print(self.pay)




class fixedtermemployee(Employee):

    def __init__(self, money):
         self.money=money

    def calculate_payroll(self):
        pay = 20.8 * 8 * self.money

    def print_info(self):
            print(self.pay)


men1=fixedtermemployee(10)
men1.calculate_payroll()
men1.print_info()



men2=fixedtermemployee(15)
men2.calculate_payroll()
men2.print_info()

