##############################################################################################
##############################       NEW CLASS       #########################################
##############################################################################################

from datetime import datetime, timedelta, date


class Job:
    
    def __init__(self, name, wage, hours, tax, deductions):
        self.name = name
        self.wage = wage
        self.hours = hours
        self.tax = tax
        self.deductions = deductions
               
    def netpay(self):
        gross_pay = self.wage * self.hours
        tax_ded = gross_pay * self.tax
        net_pay = gross_pay - tax_ded - self.deductions
        weekly_pay = net_pay
        biweekly_pay = net_pay*2
        monthly_pay = net_pay*4
        print("\n" + "-"*40)
        print(f"" +
              f"|\tEmployer: {self.name:15s}\n" + 
              f"|\tHours Worked: {self.hours}\n" +
              f"|\tPay Rate: {self.wage}\n" +
              f"|\tTaxes: {tax_ded}\n" +
              f"|\tDeductions: {self.deductions}")
        print("-"*40)
        
        
        return f"\t\t\t\t\tWeekly Pay:\t {'${:,.2f}'.format(weekly_pay)} \nBiweekly Pay:\t {'${:,.2f}'.format(biweekly_pay)} \nMonthly Pay:\t {'${:,.2f}'.format(monthly_pay)}"
    
    def return_net_pay(self):
        gross_pay = self.wage * self.hours
        tax_ded = gross_pay * self.tax
        net_pay = gross_pay - tax_ded - self.deductions
        weekly_pay = net_pay
        return weekly_pay
        
    
    def __str__(self):
        return f"Job Name: {self.name}\nJob Wage: {self.wage}"
        
    @classmethod
    def print_stub(cls):
        print("-"*25)
        
##############################################################################################
##############################       NEW CLASS       #########################################
##############################################################################################        

#class Debt:
#    debts_dict = {}
#    monthly_payments = {}
#    
#    def __init__(self, name, balance, interest, due_date, min_payment):
#        self.name = name
#        self.balance = balance
#        self.interest = interest
#        self.due_date = due_date
#        self.min_payment = min_payment
#        
#        self.add_debt()
#    
#    def add_debt(self):
#        debt_data = {
#            "Amount": self.balance,
#            "Interest": self.interest,
#            "Due_date": self.due_date,
#            "Min_payment": self.min_payment,
#        }
#        
#        Debt.debts_dict[self.name] = debt_data
#        
#    def interest_calculation(self):
#        for debt_name, debt_info in Debt.debts_dict.items():
#            
#            amount = debt_info['Amount']
#            interest_rate = debt_info['Interest']
#            
#            if interest_rate == 0:
#                amount = debt_info['Amount']
#            else:
#                interest = (interest_rate / 100 / 12) * amount
#                print(f"{interest:.2f}")
#                debt_info['Amount'] += interest
##        
#            
#        
#    @classmethod
#    def format_balance(cls):
#        for_list = []
#        final_list = []
#        for v in Debt.debts_dict.values():
#            x = f'{v["Amount"]}'
#            for_list.append(float(x))
#            
#        for i in for_list:   
#            final_list.append("${:,.2f}".format(i))
#            
#        print(final_list)
#        
#        #print("${:,.2f}".format(i))
#        #"${:,.2f}".format(min_pay_total))
#    
#    def __str__(self):
#        return f"Name: {self.name}\nBalance: {self.balance}\nInterest: {self.interest}\nDue Date: {self.due_date}\nMinimum Payment: {self.#min_payment}"
#    
#    @classmethod
#    def total_amount(cls):
#        # Calculate total balance of all debts
#        total = sum(debt_data['Amount'] for debt_data in cls.debts_dict.values())
#        
#        #sumValue = sum(d['Min_payment'] for d in Debt.debts_dict.values() if d)
#        return total
#    
#    @classmethod
#    def minimum_monthly_payments(cls):
#        # Calculate total balance of monthly minimum payments
#        total = sum(debt_data['Min_payment'] for debt_data in cls.debts_dict.values())
#        return total


##############################################################################################
##############################       NEW CLASS       #########################################
##############################################################################################

class Bill:
    bills_dict = {}
    
    def __init__(self, name, balance, due_date, min_payment):
        self.name = name
        self.balance = balance
        self.due_date = due_date
        self.min_payment = min_payment
        
        self.add_to_bills_dict()
        
    def add_to_bills_dict(self):
        bill_data = {
            "amount": self.balance,
            "due_date": self.due_date,
            "min_payment": self.min_payment,
        }
        Bill.bills_dict[self.name] = bill_data
        
    def __str__(self):
        return f"Name: {self.name:15s}\nBalance: {self.balance}\nDue Date: {self.due_date}\nMinimum Payment: {self.min_payment}"
    
    @classmethod
    def total_amount(cls):
        # Calculate total balance of all debts
        total = sum(bill_data['amount'] for bill_data in cls.bills_dict.values())
        return total
