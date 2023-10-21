from classes.bill_class import Bill
from classes.debt_class import Debt
from classes.job_class import Job

debt_data = {
    'Fortiva': {'Amount': 1071, 'Interest': 22, 'Due_date': 20, 'Min_payment': 75}, 'Capital Wal': {'Amount': 246.24, 'Interest': 0, 'Due_date': 13, 'Min_payment': 50}, 'Capital Team': {'Amount': 694.53, 'Interest': 0, 'Due_date': 13, 'Min_payment': 75}, 'Credit Cube': {'Amount': 642.11, 'Interest': 649.97, 'Due_date': 15, 'Min_payment': 271.32}, 'One Main': {'Amount': 1919, 'Interest': 40, 'Due_date': 15, 'Min_payment': 98.78}, 'MoneyLion': {'Amount': 1001, 'Interest': 20, 'Due_date': 15, 'Min_payment': 100}, 'FinWise': {'Amount': 796, 'Interest': 0, 'Due_date': 1, 'Min_payment': 100}, 'Hunt Equity': {'Amount': 16344, 'Interest': 7, 'Due_date': 28, 'Min_payment': 150}, 'Hunt Account': {'Amount': 307, 'Interest': 0, 'Due_date': 1, 'Min_payment': 50}, 'Midland': {'Amount': 5318, 'Interest': 0, 'Due_date': 1, 'Min_payment': 100}, 'Midland2': {'Amount': 700, 'Interest': 0, 'Due_date': 1, 'Min_payment': 100}, 'Plaza': {'Amount': 4217, 'Interest': 0, 'Due_date': 1, 'Min_payment': 100}, 'Jefferson': {'Amount': 6717, 'Interest': 0, 'Due_date': 1, 'Min_payment': 100}
     }

bill1 = Bill("Rent", 250, 1, 250)
bill2 = Bill("Verizon", 110, 1, 110)
bill3 = Bill("Progressive", 110, 1, 110)
bill4 = Bill("Gas", 100, 1, 100)
bill5 = Bill("Food", 200, 1, 300)
bill6 = Bill("Spending", 200, 1, 200)
    
debt1 = Debt("Fortiva", 1071, 22, 20, 75) 
debt2 = Debt("Capital Wal", 246.24, 0, 13, 50)
debt3 = Debt("Capital Team", 694.53, 0, 13, 75)
debt4 = Debt("Credit Cube", 642.11, 649.97, 15, 135.66*2)
debt5 = Debt("One Main", 1919, 40, 15, 98.78)
debt6 = Debt("MoneyLion", 1001, 20, 15, 100)
debt7 = Debt("FinWise", 796, 0, 1, 100)
debt8 = Debt("Hunt Equity", 16344, 7, 28, 150)
debt9 = Debt("Hunt Account", 307, 0, 1, 50)
debt10 = Debt("Midland", 5318, 0, 1, 100) 
debt11 = Debt("Midland2", 700, 0, 1, 100) 
debt12 = Debt("Plaza", 4217, 0, 1, 100) 
debt13 = Debt("Jefferson", 6717, 0, 1, 100) 

#d1 = "Fortiva" =
#    {'Amount': 1071, 'Interest': 22, 'Due_date': 20, 'Min_payment': 75},
#d2 = Debt.debt2  = {"Capital Wal": {'Amount': 246.24, 'Interest': 0, 'Due_date': 13, 'Min_payment': 50}}
#d3 = Debt.debt3  = {"Capital Team": {'Amount': 694.53, 'Interest': 0, 'Due_date': 13, 'Min_payment': 75}}
#d4 = Debt.debt4  = {"Credit Cube": {'Amount': 642.11, 'Interest': 649.97, 'Due_date': 15, 'Min_payment': 271.32}}
#d5 = Debt.debt5  = {"One Main": {'Amount': 1919, 'Interest': 40, 'Due_date': 15, 'Min_payment': 98.78}}
#d6 = Debt.debt6  = {"MoneyLion": {'Amount': 1001, 'Interest': 20, 'Due_date': 15, 'Min_payment': 100}}
#d7 = Debt.debt7  = {"FinWise": {'Amount': 796, 'Interest': 0, 'Due_date': 1, 'Min_payment': 100}}
#d8 = Debt.debt8  = {"Hunt Equity": {'Amount': 16344, 'Interest': 7, 'Due_date': 28, 'Min_payment': 150}}
#d9 = Debt.debt9  = {"Hunt Account": {'Amount': 307, 'Interest': 0, 'Due_date': 1, 'Min_payment': 50}}
#d10 = Debt.debt10 = {"Midland": {'Amount': 5318, 'Interest': 0, 'Due_date': 1, 'Min_payment': 100}}
#d11 = Debt.debt11 = {"Midland2": {'Amount': 700, 'Interest': 0, 'Due_date': 1, 'Min_payment': 100}}
#d12 = Debt.debt12 = {"Plaza": {'Amount': 4217, 'Interest': 0, 'Due_date': 1, 'Min_payment': 100}}
#d13 = Debt.debt13 = {"Jefferson": {'Amount': 6717, 'Interest': 0, 'Due_date': 1, 'Min_payment': 100}}

job1 = Job("UPS", 21, 10, .11700086, 50)
job2 = Job("HTC", 22, 40, .12, 89.08)

#bill1 = Bill("Rent", 250, 1, 250)
#bill2 = Bill("Verizon", 110, 1, 110)
#bill3 = Bill("Progressive", 110, 1, 110)
#    
#debt1 = Debt("Fortiva", 1071, 22, 20, 75) 
#debt2 = Debt("Capital Wal", 246.24, 0, 13, 50)
#debt3 = Debt("Capital Team", 694.53, 0, 13, 75)
#debt4 = Debt("Credit Cube", 642.11, 649.97, 15, 135.66*2)
#debt5 = Debt("One Main", 1919, 40, 15, 98.78)
#debt6 = Debt("MoneyLion", 1001, 20, 15, 100)
#debt7 = Debt("FinWise", 796, 0, 1, 100)
#debt8 = Debt("Hunt Equity", 16344, 7, 28, 150)
#debt9 = Debt("Hunt Account", 307, 0, 1, 50)
#debt10 = Debt("Midland", 5318, 0, 1, 100) 
#debt11 = Debt("Midland2", 700, 0, 1, 100) 
#debt12 = Debt("Plaza", 4217, 0, 1, 100) 
#debt13 = Debt("Jefferson", 6717, 0, 1, 100) 
#
##debt1 = Debt(Fortiva         : {'Amount': 1071, 'Interest': 22, 'Due_date': 20, 'Min_payment': 75})
##debt2 = Debt(Capital Wal     : {'Amount': 246.24, 'Interest': 0, 'Due_date': 13, 'Min_payment': 50})
##debt3 = Debt(Capital Team    : {'Amount': 694.53, 'Interest': 0, 'Due_date': 13, 'Min_payment': 75})
##debt4 = Debt(Credit Cube     : {'Amount': 642.11, 'Interest': 649.97, 'Due_date': 15, 'Min_payment': 271.32})
##debt5 = Debt(One Main        : {'Amount': 1919, 'Interest': 40, 'Due_date': 15, 'Min_payment': 98.78})
##debt6 = Debt(MoneyLion       : {'Amount': 1001, 'Interest': 20, 'Due_date': 15, 'Min_payment': 100})
##debt7 = Debt(FinWise         : {'Amount': 796, 'Interest': 0, 'Due_date': 1, 'Min_payment': 100})
##debt8 = Debt(Hunt Equity     : {'Amount': 16344, 'Interest': 7, 'Due_date': 28, 'Min_payment': 150})
##debt9 = Debt(Hunt Account    : {'Amount': 307, 'Interest': 0, 'Due_date': 1, 'Min_payment': 50})
##debt10 = Debt(Midland         : {'Amount': 5318, 'Interest': 0, 'Due_date': 1, 'Min_payment': 100})
##debt11 = Debt(Midland2        : {'Amount': 700, 'Interest': 0, 'Due_date': 1, 'Min_payment': 100})
##debt12 = Debt(Plaza           : {'Amount': 4217, 'Interest': 0, 'Due_date': 1, 'Min_payment': 100})
##debt13 = Debt(Jefferson : {'Amount': 6717, 'Interest': 0, 'Due_date': 1, 'Min_payment': 100})
#
#job1 = Job("UPS", 21, 10, .11700086, 50)
#job2 = Job("HTC", 22, 40, .1761856, 178.16/2)