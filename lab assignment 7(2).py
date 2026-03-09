balance = 0

def show_balance():
    print("Current Balance =", balance)

def deposit(amount):
    global balance
    balance += amount
    print("Amount Deposited Successfully")

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient Balance")
    else:
        balance -= amount
        print("Withdrawal Successful")


while True:
    print("\n--- BANK MENU ---")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 4:
        print("Thank you")
        break

    if choice == 1:
        show_balance()
    elif choice == 2:
        amt = float(input("Enter amount to deposit: "))
        deposit(amt)
    elif choice == 3:
        amt = float(input("Enter amount to withdraw: "))
        withdraw(amt)
    else:
        print("Invalid choice")
