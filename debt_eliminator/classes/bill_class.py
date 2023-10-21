

class Bill:
    bill_data = {}
    
    def __init__(self, name, balance, due_date, min_payment):
        self.name = name
        self.balance = balance
        self.due_date = due_date
        self.min_payment = min_payment
        self.add_bill()
        
    def add_bill(self):
        self.bill_data[self.name] = {
            "Balance": self.balance,
            "Due_date": self.due_date,
            "Min_payment": self.min_payment
        }

    def remove_bill(self, bill_data, bill_name):
        if bill_name in bill_data:
            del bill_data[bill_name]
            print(f"{bill_name} has been removed. ")
        else:
            print(f"{bill_name} not found in the bill data. ")
            
    @classmethod
    def print_bill(self, bill_data):
        for bill_name, bill_info in bill_data.items():
            balance = bill_info['Balance']
            min_pay = bill_info['Min_payment']
            print(f"{bill_name:<15}: {balance:^12,.2f}{min_pay:>15,.2f}")
    
    def __str__(self):
        return f"Name: {self.name:15s}\nBalance: {self.balance}\nDue Date: {self.due_date}\nMinimum Payment: {self.min_payment}"
    
    @classmethod
    def add_bill_from_input(cls):
        name = input("Enter the name of the bill: ")
        balance = float(input("Enter the balance of the bill: "))
        due_date = int(input("Enter the payment due date each month: "))
        min_payment = float(input("Enter the minimum monthly payment: "))
        
        new_bill = cls(name, balance, due_date, min_payment)
        print(f"{name} bill has been added")
    
    @classmethod
    def total_amount(cls):
        # Calculate total balance of all bills
        total = sum(bill_data['amount'] for bill_data in cls.bill_data.values())
        return total

    @classmethod
    def minimum_monthly_payments(cls):
        # Calculate total balance of monthly minimum payments
        total = sum(bill_data['Min_payment'] for bill_data in cls.bill_data.values())
        return total