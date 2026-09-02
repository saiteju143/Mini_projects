bank_details=[]


while True:

    print("BANKING APPLICATION \n")
    print("1.Create Acc")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Check_balance")
    print("5.Transfer_money")
    print("6.Show_accounts")
    print("7.Exit")


    choice=int(input("enter choice"))
    if choice==1:
        while True:
            account_number=input("enter acc_nunber(or 'done' if finished)")
            if account_number=="done":
                break
            if any(account["acc_number"] ==account_number for account in bank_details):
                print("Acc_number already exists.Enter another acc_number")
                continue
            else:
                name=input("enter acc_holder name")
                balance=float(input("enter acc_balance"))
                bank_details.append({"acc_number":account_number , "name":name,"avl_balance":balance})

    elif choice==2:
        account_number = input("Enter account number: ")
        deposit_amount=int(input("enter amount to deposit:"))
        if deposit_amount <=0:
            print("Deposit amount should be positive")
        else:
            for bal in bank_details:
                if bal["acc_number"]==account_number:
                    bal["avl_balance"]+=deposit_amount
                    print("Amount deposited successfully")
                    break
            else:
                print("Acc num not found")
            

    elif choice==3:
        account_number = input("Enter account number: ")
        withdraw_amount=int(input("enter amount to withdraw"))
        for bal in bank_details:
            if bal["acc_number"]==account_number:
                if withdraw_amount>bal["avl_balance"]:
                    print("Transaction declined")
                    
                else:
                    bal["avl_balance"]-=withdraw_amount
                    print("Amount wothdrawn successfully")
                break
        else:
            print("Acc not found")
    elif choice==4:
        account_number = input("Enter account number: ")
        for bal in bank_details:
            if bal["acc_number"]==account_number:
                print("name:", bal["name"])
                print("balance:", bal["avl_balance"])
                break
        else:
            print("Acc not found")
    elif choice==5:
        source_acc=input("enter source acc_num")
        target_acc=input("enter target acc_num")
        amount=int(input("enter amount to transfer"))
        source=None
        Target=None
        for bal in bank_details:
            if bal["acc_number"]==source_acc:
                source=bal
            if bal["acc_number"]==target_acc:
                Target=bal
        if source and Target:
            if source["avl_balance"]>=amount:
                source["avl_balance"]-=amount
                Target["avl_balance"]+=amount
                print("Transfer successful")
            else:
                print("Insufficeint balance")
        else:
            print("invalid acc_number")
    elif choice==6:
        for bal in bank_details:
            print(bal)
        total_money=0
        highest_bal=0
        rich_customer=""
        for bal in bank_details:
            total_money+=bal["avl_balance"]
            if bal["avl_balance"]>highest_bal:
                highest_bal=bal["avl_balance"]
                rich_customer=bal["name"]

        print("Total_money in bank:" , total_money)
        print("Rich customer in bank:",rich_customer)
    elif choice==7:
        print("Exiting bank system")
        print("Exit")
        break





                    



