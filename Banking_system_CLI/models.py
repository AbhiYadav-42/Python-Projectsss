"""To-do list"""
#->Create Account class
  #-> Add attributes: account_number, balance

#-> Add methods:
  #->deposit()
  #-> withdraw()
  #-> check_balance()

#User class (name, user_id, accounts list)

#-> Bank class
  #-> Bank method:
    #-> create_user()
    #-> create_account()
    #-> find_account()
    #-> transfer()


class Account:
  def __init__(self, acc_num, inital_bal = 0 ):
    self.acc_num = acc_num
    self.bal = inital_bal


  def acc_deposit(self, amount):
    if amount<=0:
      print("Amount must be in +ve")
      return
    self.bal += amount
    print("Amount has been DEPOSITED!!")


  def acc_withdraw(self, amount):
    if amount<=0:
      print("amount must been in +ve")
      return
    if amount> self.bal:
      print("insufficeint bal, CAN'T withdraw!!")
      return
    self.bal -=  amount
    print("Amount withdrawn!!")


  def ch_bal(self,):
    print(f"balance: {self.bal} ")
    return self.bal


class User:
  def __init__(self, name, user_id, ):
    self.name = name
    self.user_id = user_id
    self.acc_list = [] 

  def add_account(self, account):
    self.acc_list.append(account)

class Bank:
  def __init__(self ):
    self.user_dic = {}     # user_id -> user
    self.account_dic ={}   # acc_num  -> account

  def create_user(self,name, user_id):
    user =  User(name, user_id)     # object created
    self.user_dic[user_id] = user       # add in the user dic
    
    print(f" User {name} CREATED!!")
    return user

  def create_account(self,user_id,acc_num, inital_bal =0):
    account = Account( acc_num,inital_bal)
    self.account_dic[acc_num] = account
    self.user_dic[user_id].add_account(account)
    
    print(f"Account {acc_num} created for user {user_id} ")
    return account

  def find_acc(self,acc_num):
    return self.account_dic.get(acc_num, None)


  def transfer(self, from_acc_num, to_acc_num, amount):
    from_find = self.find_acc(from_acc_num) 
    to_find = self.find_acc(to_acc_num)
    
    #subtract
    from_find.bal -= amount
    to_find.bal += amount
    print(f"Transferred {amount} from {from_acc_num} to {to_acc_num}. ")
    