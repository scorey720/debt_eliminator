
class FinancialEntity:
    debt_data = {}
    
    def __init__(self, name, balance, interest, due_date, min_payment):
        self.name = name
        self.balance = balance
        self.interest = interest
        self.due_date = due_date
        self.min_payment = min_payment
        self.add_entity()
        
    def add_entity(self):
        self.debt_data[self.name] = {
            'Balance': self.balance,
            'Interest': self.interest,
            'Due_date': self.due_date,
            'Min_payment': self.min_payment
        }
        