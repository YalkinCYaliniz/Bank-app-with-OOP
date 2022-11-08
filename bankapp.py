#Some exercies with OOP
from curses.ascii import isdigit

class account:
    def __init__(self,name,password,balance):
        self.name = name
        self.password = password
        self.balance = balance
                
class bankSystem(account):
    def __init__(self, name, password, balance,case,withM):
        super().__init__(name, password, balance)
        self.case = case
        self.withM = withM
    def addMoney(self,money):
        self.money = money
        self.balance += money
        return("You added {} and now your balance {}".format(self.money,self.balance))
    def withdrawMoney(self,withM):
        
        if newUser.withM > newUser.balance or newUser.balance == 0:
            return("You cant withdraw it, because your balance is lowwer than withdraw moneys")
        else:    
            self.balance -= withM
            return(f"You withdrawed {withM} and now you have {self.balance}")
        
    def checkPassword(self,nPassword):
        self.npass = nPassword
        for passwordtry in range(3):
            self.npass = input("Please write your password: ")
            if self.password == self.npass:
                print(f"Succesfull login! You logged on the {passwordtry+1}. try")  
                break                   
            if nPassword.isdigit == 0:
                raise ValueError("Please write your password with numbers")
                
            if len(self.npass) < 4 or len(self.npass) > 4:
                raise ValueError("Please write your password with four numbers")    
            if self.password != self.npass:
                print("You wrote wrong password,please try again")                                           
            if passwordtry == 3:
                print("System ended")
            
newUser = bankSystem("admin","1212",1000,case=0,withM=0) 
newUser.checkPassword("1212")
exitKey = ' '
while exitKey != "n" and exitKey != "N":
    case = int(input("Select your process \n 1-) Withdraw Money \n 2-) Learn your balance \n 3-) Add Money \n "))
    if case == 1:
        newUser.withM = int(input("How much money will you withdraw? "))    
        print(newUser.withdrawMoney(withM=newUser.withM))
    elif case == 2:
        print(newUser.balance)    
    elif case == 3:
        print(newUser.addMoney(int(input("How much money will you add to you balance? "))))   
    exitKey = input("If you want to exit, please press n or N. If you dont want to exit please any button!  ")
print("System ended!")
    