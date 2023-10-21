

class Job():
    job_data = {}
    
    def __init__(self, name, wage, hours, tax, deductions):
        self.name = name
        self.wage = wage
        self.hours = hours
        self.tax = tax
        self.deductions = deductions
        self.add_job_data()
        
    def add_job_data(self):
        self.job_data[self.name] = {
            'Wage': self.wage,
            'Hours': self.hours,
            'Tax': self.tax,
            'Deductions': self.deductions
        }
    
    @classmethod
    def print_job(self, job_data):
        for job_name, job_info in job_data.items():
            wage = job_info['Wage']
            hours = job_info['Hours']
            print(f"{job_name:<15}: {wage:^12,.2f} {hours:>13,.2f}")

            
             
    def netpay(job_data):
        for job_name, job_info in job_data.items():
            wage = job_info['Wage']
            hours = job_info['Hours']
            tax = job_info['Tax']
            deductions = job_info['Deductions']
            
            gross_pay = wage * hours
            tax_ded = gross_pay * tax
            net_pay = gross_pay - tax_ded - deductions
            weekly_pay = net_pay
            biweekly_pay = net_pay*2
            monthly_pay = net_pay*4
            print("\n" + "-"*40)
            print(f"" +
                  f"|\tEmployer: {job_name:15s}\n" + 
                  f"|\tHours Worked: {hours}\n" +
                  f"|\tPay Rate: {wage}\n" +
                  f"|\tTaxes: {tax_ded}\n" +
                  f"|\tDeductions: {deductions}")
            print("-"*40)
            print(f"Weekly Pay:\t {'${:,.2f}'.format(weekly_pay)} \nBiweekly Pay:\t {'${:,.2f}'.format(biweekly_pay)} \nMonthly Pay:\t {'${:,.2f}'.format(monthly_pay)}")
    
    def return_net_pay(self):
        gross_pay = self.wage * self.hours
        tax_ded = gross_pay * self.tax
        net_pay = gross_pay - tax_ded - self.deductions
        weekly_pay = net_pay
        return weekly_pay
        
    
    def __str__(self):
        return f"Job Name: {self.name}\nJob Wage: {self.wage}"
        
    @classmethod
    def add_job_input(cls):
        name = input(f"Enter the name of the job: ")
        wage = float(input("Enter your hourly wages: "))
        hours = float(input("Enter how many hours per week: "))
        tax = float(input("Enter your tax rate: "))
        deductions = float(input("Enter your deductions amount: "))
        
        new_job = cls(name, wage, hours, tax, deductions)
        print(f"{name} job has been added. ")