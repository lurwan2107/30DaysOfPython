# EXERCISE LEVEL 2

class PersonAccount:
    
    
    def __init__(self, firstname, lastname, incomes, expenses_prop):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses_prop
        self.total = 0
        self.total1 = 0

    def total_income(self):
        incm = dict(self.incomes)
        print('The descriptions of the incomes are as follows:')
        for key, value in incm.items():
           
            print(f'\tIncome from {key} is {value}$')
            self.total += value
        print(f'The total income is: {self.total}$\n')

    def total_expenses(self):
        spend = dict(self.expenses)
        print('The descriptions of expenses are as follows:')
        for key, value in spend.items():
            print('\tWe bought {} for {}$'.format(key, value))
            self.total1 += value
        print(f'The total expenses is: {self.total1}$\n')

    def account_info(self):
        print('   Account Information')
        print('   -------------------')
        print(f'Firstname: {self.firstname}')
        print(f'Lastname : {self.lastname}\n')

    def add_income(self):
        num1 = 0
        addIncome = dict(self.incomes)
        for k, v in addIncome.items():
            num1 += v
        print('If you add the incomes you will get: {}$\n'.format(num1))


    def add_expenses(self):
        num2 = 0
        addExpenses = dict(self.expenses)
        for A, E in addExpenses.items():
            num2 += E
        print('The sum of the overall expenses is {}$\n'.format(num2))

    def account_balance(self):
        print('   Account Balance')
        print('   ---------------')
        balance1 = 0
        balance2 = 0
        income = dict(self.incomes)
        subtract = dict(self.expenses)
        for k, v in income.items():
            balance1 += v
        print('Our account balance before is:')
        print("Account balance: {:.2f}".format(balance1))
        for i, j in subtract.items():
            balance2 += j
        print('Our account balance now is:')
        print('Account balance: {:.2f}\n'.format(balance1 - balance2))
        

account = PersonAccount('Lurwan', 'Abdullahi', {'Oil company':20000, 'Foultry Farm':14000, 'Industry':7000}, {'Apple':3000, 'Rice':8000, 'Beans':4000})
account.total_income()
account.total_expenses()
account.account_info()
account.add_income()
account.add_expenses()
account.account_balance()