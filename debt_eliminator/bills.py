from bill_class import Job, Bill
from bill_data import *

bill_total = Bill.total_amount()
min_pay_total = Debt.minimum_monthly_payments()

debt_data = {
    'Fortiva': {'Amount': 1071, 'Interest': 22, 'Due_date': 20, 'Min_payment': 75}, 'Capital Wal': {'Amount': 246.24, 'Interest': 0, 'Due_date': 13, 'Min_payment': 50}, 'Capital Team': {'Amount': 694.53, 'Interest': 0, 'Due_date': 13, 'Min_payment': 75}, 'Credit Cube': {'Amount': 642.11, 'Interest': 649.97, 'Due_date': 15, 'Min_payment': 271.32}, 'One Main': {'Amount': 1919, 'Interest': 40, 'Due_date': 15, 'Min_payment': 98.78}, 'MoneyLion': {'Amount': 1001, 'Interest': 20, 'Due_date': 15, 'Min_payment': 100}, 'FinWise': {'Amount': 796, 'Interest': 0, 'Due_date': 1, 'Min_payment': 100}, 'Hunt Equity': {'Amount': 16344, 'Interest': 7, 'Due_date': 28, 'Min_payment': 150}, 'Hunt Account': {'Amount': 307, 'Interest': 0, 'Due_date': 1, 'Min_payment': 50}, 'Midland': {'Amount': 5318, 'Interest': 0, 'Due_date': 1, 'Min_payment': 100}, 'Midland2': {'Amount': 700, 'Interest': 0, 'Due_date': 1, 'Min_payment': 100}, 'Plaza': {'Amount': 4217, 'Interest': 0, 'Due_date': 1, 'Min_payment': 100}, 'Jefferson': {'Amount': 6717, 'Interest': 0, 'Due_date': 1, 'Min_payment': 100}
     }

def net_wages():
    wage1 = job1.return_net_pay()
    wage2 = job2.return_net_pay()
    net_pay = wage1 + wage2
    net_pay = net_pay * 4
    return net_pay

def order_debts_by_amount(updated_debt_data):
    # Creatte a list of debts with (data_name, amount)
    debts_with_amounts = [(debt_name, debt_info['Amount']) for debt_name, debt_info in updated_debt_data.items()]
    sorted_debts = sorted(debts_with_amounts, key=lambda x: x[1])
    return sorted_debts

def update_debt_amount(debt_data):
    updated_debt_data = {}
    for debt_name, debt_info in debt_data.items():
        amount = debt_info['Amount']
        min_payment = debt_info['Min_payment']
        updated_amount = amount - min_payment
        print(f"{debt_name}: ${amount:.2f} - ${min_payment:.2f}")
        if updated_amount < 0:
            updated_amount = 0
        debt_info['Amount'] = updated_amount
        updated_debt_data[debt_name] = debt_info
    return updated_debt_data

def get_monthly_pay(bill_total, min_pay_total):
    monthly_payments = bill_total + min_pay_total
    print(f"\nMonthly Debts / Bill Total: ${monthly_payments:.2f}\n")
    return monthly_payments

def left_over_pay(monthly_income, monthly_debt_payments):
    left_over = monthly_income - monthly_debt_payments
    print(f"Money Left over after bills/debts paid: ${left_over:.2f}\n")
    return left_over

def get_lowest_balance(updated_debt_data):
    lowest_amount = None
    lowest_debt_name = None
    
    for debt_name, debt_info in updated_debt_data.items():
        amount = debt_info['Amount']
        if lowest_amount is None or amount < lowest_amount:
            lowest_amount = amount
            lowest_debt_name = debt_name
    if lowest_debt_name is not None:
        print(f"\n\nThe debt with the lowest about is {lowest_debt_name}: ${lowest_amount:.2f}\n\n")
    else:
        print("No debts found in the data")
    return lowest_amount

def subtract_left_over_from_debt(updated_debt_data, left_over):
    debts_with_amounts = [(debt_name, debt_info['Amount']) for debt_name, debt_info in updated_debt_data.items()]
    sorted_debts = sorted(debts_with_amounts, key=lambda x: x[1])
    
    remaining_amount = left_over
    
    for debt_name, amount in sorted_debts:
        if remaining_amount <= 0:
            break
        current_debt = updated_debt_data[debt_name]
        current_debt_amount = current_debt['Amount']
        
        new_debt_amount = max(current_debt_amount - remaining_amount, 0)
        remaining_amount -= (current_debt_amount - new_debt_amount)
        
        current_debt['Amount'] = new_debt_amount
        
        print(f"Subtracted ${current_debt_amount - new_debt_amount:.2f} from {debt_name}, "
              f"new amount: ${new_debt_amount:.2f}\n")    
        
    return updated_debt_data

def calculate_total_balance(updated_debt_data):
    #total = Debt.total_amount(updated_debt_data)
    total_balance = sum(debt_info['Amount'] for debt_info in updated_debt_data.values())
    return total_balance

def calculate_total_min_payments(updated_debt_data):
    #total = Debt.minimum_monthly_payments(updated_debt_data)
    total_min_pay = sum(debt_info['Min_payment'] for debt_info in updated_debt_data.values())
    return total_min_pay
    
def remove_zero_debt(updated_debt_data, paid_off_debts):
    debts_to_remove = []
    
    for debt_name, debt_info in updated_debt_data.items():
        amount = debt_info['Amount']
        
        if amount == 0:
            paid_off_debts[debt_name] = debt_info
            debts_to_remove.append(debt_name)
            
    for debt_name in debts_to_remove:
        del updated_debt_data[debt_name]
    
    return updated_debt_data
      
def main(debt_data):
    bill_total = Bill.total_amount()
    min_pay_total = Debt.minimum_monthly_payments()
    print("-----------BEGIN--------------")
    
    paid_off_debts = {}
    monthly_income = net_wages()
    new_balance_total = calculate_total_balance(debt_data)
    months = 0
    next = True
    while new_balance_total > 0:
        
        monthly_debt_payments = get_monthly_pay(bill_total, min_pay_total)
        
        left_over = left_over_pay(monthly_income, monthly_debt_payments)
        
        updated_debt_data = update_debt_amount(debt_data)
        
        order_debts_by_amount(updated_debt_data)
        
        lowest_balance = get_lowest_balance(updated_debt_data)
        
        subtract_left_over_from_debt(updated_debt_data, left_over)
                
        remove_zero_debt(updated_debt_data, paid_off_debts)
        
        order_debts_by_amount(updated_debt_data)
        
        months += 1
        
        new_balance_total = calculate_total_balance(updated_debt_data)
        
        min_pay_total = calculate_total_min_payments(updated_debt_data)
        
        next = input("Continue to next Pay Period?: ")
        
        if next != 'y' or 'Y':
            
            next = False
        
        
    print(months)


if __name__ == "__main__":
    main(debt_data)