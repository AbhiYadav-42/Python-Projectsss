from models import Bank


def bank_system():
  bank = Bank()
  balance = 0
  while True:
    print("\n----- Bank System ------")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer Money")
    print("5. Create User")
    print("6. Create Account")
    print("7. EXIT")


    choice = input("Enter choice (1,7): ")

    if choice == '1':
      in_put = input("Enter your Account number: ")
      account = bank.find_acc(in_put)
      if account is None:
        print("Account not found. ")
      else:
        account.ch_bal()

    elif choice == '2':
      in_put = input("Enter your Account number: ")
      account = bank.find_acc(in_put)
      
      if account is None:
        print("account not found!")
      else:
        amount = float(input("Enter deposit amount: "))
        account.acc_deposit(amount)

    elif choice == '3':
      in_put = input("Enter your Account number: ")
      account = bank.find_acc(in_put)
      
      if account is None:
        print("account not found!")
      else:
        amount = float(input("Enter withdraw amount: "))
        account.acc_withdraw(amount)

    elif choice == '4':
      in_put = input("Enter your Account number: ")
      to_acc = input("Transfer account number: ")
      
      account = bank.find_acc(in_put)
      to_account = bank.find_acc(to_acc)
      
      if account is None or  to_account is None:
        print("account not found!")
      else:
        amount = float(input("Enter withdraw amount: "))
        bank.transfer(in_put,to_acc,amount)

    elif choice == '5':
      in_put = input("Enter name: ")
      usr_id = input("Enter adhar number: ")
      if usr_id in bank.user_dic:
        print("user_id exist!, not eligible for creating user ")
      else:
        bank.create_user(in_put,usr_id)

    elif choice == '6':
      print("IT is adivisable to create user first then ACC creation\n")
      usr_id = input("Enter adhar number: ")
      cash = float(input("Enter the inital amount: "))
      if usr_id in bank.user_dic:
        acc_num = f"ACC" + str(len(bank.account_dic)+1 )
        print(f"account Number has been gernated!!")
        bank.create_account(usr_id,acc_num,cash)
        
      else:
        print("User not found. Please create a user first ")

    elif choice == '7':
      print("Thank You! ")
      return None

bank_system()