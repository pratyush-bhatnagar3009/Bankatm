import random
class atm:
    def __init__(self,balanceenquiry,cashwithdrawl,creditscore):
        self.balanceenquiry = balanceenquiry
        self.cashwithdrawl = cashwithdrawl
        self.creditscore = creditscore

def balance():
    var bankbalance = random.randint(1,10000000)
    print('Your balance is'+ bankbalance)

def cashwithdrawl():
    cash = input('How much would you like to withdraw from your account?')
    if cash > 500:
        print('That is too high a value.')
    if cash < 50:
        print('That is too low a value')
    if 500>cash>50:
        print(cash + 'has been withdrawn from your account.')

def credit():
    var personcredit = random.randint(1,100)
    print('Your credit score is '+ personcredit)