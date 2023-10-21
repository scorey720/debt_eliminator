import csv
from prettytable import PrettyTable


class Debt():
    debt_data = {}
    
    def __init__(self, name, balance, interest, due_date, min_payment):
        self.name = name
        self.balance = balance
        self.interest = interest
        self.due_date = due_date
        self.min_payment = min_payment
        self.add_debt()

    def add_debt(self):
        self.debt_data[self.name] = {
            'Balance': self.balance,
            'Interest': self.interest,
            'Due_date': self.due_date,
            'Min_payment': self.min_payment
        }
        
    def remove_debt(self, debt_data, debt_name):
        if debt_name in debt_data:
            del debt_data[debt_name]
            print(f"{debt_name} has been removed. ")
        else:
            print(f"{debt_name} not found in the debt data. ")
    
    def calculate_total_debt(self):
        pass
    
    def calculate_interest(self):
        pass
    
    def subtract_minimum_payment(self):
        pass
    
    def calculate_monthly_payments(self):
        pass
    
    def print_debt(debt_data):
        
        for debt_name, debt_info in debt_data.items():
            balance = debt_info['Balance']
            min_pay = debt_info['Min_payment']
            print(f"{debt_name:<15}: {balance:^12,.2f}{min_pay:>15,.2f}")
    
    @classmethod
    def add_debt_from_input(cls):
        name = input("Enter the name of the debt: ")
        balance = float(input("Enter the balance of the Debt: "))
        interest = float(input("Enter the interest rate as a whole number: "))
        due_date = int(input("Enter the payment due date each month: "))
        min_payment = float(input("Enter the minimum monthly payment: "))
        
        new_debt = cls(name, balance, interest, due_date, min_payment)
        print(f"{name} debt has been added")
         
    def __str__(self):
        return f"Name: {self.name}\nBalance: {self.balance}\nInterest: {self.interest}\nDue Date: {self.due_date}\nMinimum Payment: {self.min_payment}"

    @classmethod
    def format_balance(cls):
        for_list = []
        final_list = []
        for v in Debt.debt_data.values():
            x = f'{v["Balance"]}'
            for_list.append(float(x))
            
        for i in for_list:   
            final_list.append("${:,.2f}".format(i))
            
        print(final_list)
        
        #print("${:,.2f}".format(i))
        #"${:,.2f}".format(min_pay_total))
  
    @classmethod
    def total_amount(cls):
        # Calculate total balance of all debts
        total = sum(debt_data['Balance'] for debt_data in cls.debt_data.values())
        
        #sumValue = sum(d['Min_payment'] for d in Debt.debt_data.values() if d)
        return total
    
    @classmethod
    def minimum_monthly_payments(cls):
        # Calculate total balance of monthly minimum payments
        total = sum(debt_data['Min_payment'] for debt_data in cls.debt_data.values())
        return total
    
    @classmethod
    def update_debt_element(cls):
        debt_name = input("Enter the name of the debt to append:  ")
        if debt_name in cls.debt_data:
            print(f"Choose an element to udpate for '{debt_name}': ")
            print(" 1. Balance")
            print(" 2. Interest")
            print(" 3. Due Date")
            print(" 4. Minimum Payment")
            choice = input("Enter the name of the element to update: ")
            
            if choice == "1":
                new_balance = float(input(f"Enter the new balance for {debt_name}: "))
                cls.debt_data[debt_name]['Balance'] = new_balance
            
            elif choice == "2":
                new_interest = float(input(f"Enter the new interest for {debt_name}: "))
                cls.debt_data[debt_name]['Interest'] = new_interest
                
            elif choice == "3":
                new_due_date = int(input(f"Enter the new Due Date for {debt_name}: "))
                cls.debt_data[debt_name]['Due_Date'] = new_due_date
                
            elif choice == "4":
                new_min_payment = float(input(f"Enter the new Minimum Payment for {debt_name}: "))
                cls.debt_data[debt_name]['Min_payment'] = new_min_payment
                
            else:
                print("Invalid choice.")
                
        else:
            print(f"'{debt_name}' debt not found")
            
    @classmethod
    def save_debt_data(cls, filename):
        with open(filename,'w', newline='') as csvfile:
            fieldnames = ['Name', 'Balance', 'Interest', 'Due_date', 'Min_payment']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for debt_name, debt_details in cls.debt_data.items():
                writer.writerwo({
                    'Name': debt_name,
                    'Balance': debt_details['Balance'],
                    'Interest': debt_details['Interest'],
                    'Due_date': debt_details['Due_date'],
                    'Min_payment': debt_details['Min_payment']
                })
        
        print(f"Debt data has been saved to {filename} in CSV format. ")
        
    @classmethod
    def load_debt_data(cls, filename):
        try:
            with open(filename, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                cls.debt_data = {}
                for row in reader:
                    cls.debt_data[row['Name']] = {
                        'Balance': float(row['Balance']),
                        'Interest': float(row['Interest']),
                        'Due_date': int(row['Due_date']),
                        'Min_payment': float(row['Min_payment'])
                    }
                print(f"Debt data has been loaded from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with empty Data. ")
        except Exception as e:
            print(f"An error occurred while loading data: {str(e)}")
        
    @classmethod
    def debt_collate(cls):
        table = PrettyTable()
        table.field_names = ["Lender", "Balance", "Interest", "Due Date", "Minimum Payment"]
        
        for lender, data in Debt.debt_data.items():
            balance = f"${data['Balance']:.2f}"
            interest = f"${data['Interest']:.2f}"
            due_date = data['Due_date']
            min_payment = f"${data['Min_payment']:.2f}"
            
            table.add_row([lender, balance, interest, due_date, min_payment])
            
        print(table)
            