# Python banking program

# 1. Show Balance
# 2. Deposit
# 3. Withdraw


def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")


def deposit():
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0:
        print("That's not a valid amount")
        return 0
    else:
        return amount


def withdraw(balance):
    amount = float(input("Enter an amount to be withdrawn: "))

    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("That is not a valid choice")

    print("Thank you! Have a nice day!")


if __name__ == "__main__":
    main()
