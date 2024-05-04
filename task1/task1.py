account_numbers = ['8053171777', '9034567734', '8134526791', '8034541881', '9121541959']
capital_amount = 500
account_number = input("Which account number do you want to deposit to?: ")
while account_number not in account_numbers:
    account_number = input(f"There is no account with {account_number} in our database, try again.")
    if account_number in account_numbers:
        pass
if account_number in account_numbers:
    amount = int(input("How much do you want to deposit: "))
    if amount < 0:
        print("invalid")
    else:
        total_amount = capital_amount + amount
        print(f'The total amount in {account_number} is ${total_amount}.')

