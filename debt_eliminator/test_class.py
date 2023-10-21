#/Users/shizz/Projects/python_virt/myenv/bin/activate
from classes.job_class import Job
from classes.bill_class import Bill
from classes.debt_class import Debt
from bill_data import *
def main():
    
    choice = 0
    while True:
        print(f"\nWelcome to the Vill Collector!  \n")
        print("Choose an option! \n")   
        print(" 1. Add a new Debt: ")
        print(" 2. Add a new Bill: ")
        print(" 3. Add a new Job: ")
        print(" 4. Remove a Debt: ")
        print(" 5. Remove a Bill: ")
        print(" 6. Remove a Job: ")
        print(" 7. Append an element: ")
        print(" 8. Display the list: ")
        print(" 9. Calculate Total Debt: ")
        print(" 10. Display the list: ")
        print(" 11. Save Existing Data: ")
        print(" 12. Open Data File: ")
        print(" 13. Exit: ")
        
        choice = int(input("\nEnter Your Choice (1-13):  "))
        
        if choice == 1:
            Debt.add_debt_from_input()
            
        elif choice == 2: 
            Bill.add_bill_from_input()
            print(Bill.bill_data)
        
        elif choice == 3: 
            Job.add_job_input()
            print(Job.job_data)
        
        elif choice == 4: 
            remove = input("Enter the name of the Debt you want to remove: ")
            try:
                Debt.remove_debt(Debt.debt_data, remove)
            except:
                print("That Debt was not found! ")
                
        elif choice == 5: 
            Job.netpay(Job.job_data)
        
        elif choice == 6: 
            pass
        
        elif choice == 7: 
            Debt.update_debt_element()
        
        elif choice == 8: 
            Debt.print_debt(Debt.debt_data)
            Bill.print_bill(Bill.bill_data)
            Job.print_job(Job.job_data)
        
        elif choice == 9: 
            Debt.total_amount()
        
        elif choice == 10: 
            Debt.debt_collate()
        
        elif choice == 11:
            extention = '.csv'
            filename = input("Enter name for save file: ") + extention
            Debt.save_debt_data(filename)
            
        elif choice == 12: 
            extention = '.csv'
            filename = input("Enter name of saved file with out the .csv: ")
            Debt.load_debt_data(filename)
            
        elif choice == 13: 
            exit()

if __name__ == '__main__':
    main()

#ups = job1
#htc = job2
#Debt.add_debt_from_input()
#print(Debt.debt_data)
#Debt.format_balance()
#def add_debt(debt_data, debt_name, debt_details):
#    debt_data[debt_name] = debt_details
# #new_debt = {
#    'Amount': 1234,
#    'Interest': 56.78,
#    'Due_date': 10,
#    'Min_payment': 75.50
#}
##ndebt = Debt('NewDebt', new_debt['Amount'], new_debt['Interest'], new_debt['Due_date'], new_debt['Min_payment'])
#
#Debt.remove_debt(Debt.debt_data, 'balls')    
#Debt.remove_debt(Debt.debt_data, 'balls')     
 #print(Debt.debt_data)