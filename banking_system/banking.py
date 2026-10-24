from datetime import datetime

class BankAccount:
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        self.balance = round(self.balance + amount, 2)
        self.transactions.append(
            f"Deposit: Rs. {amount:.2f}"
        )
        print("Deposit successful!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance = round(self.balance - amount, 2)
            self.transactions.append(
                f"Withdrawal: Rs. {amount:.2f}"
            )
            print("Withdrawal successful!")

    def show_balance(self):
        print(f"Account holder: {self.name}")
        print(f"Current balance: Rs. {self.balance:.2f}")

    def show_transactions(self):
        print("\n--- Transaction History ---")
        if not self.transactions:
            print("No transactions yet.")
        else:
            for transaction in self.transactions:
                print(transaction)


def main():
    print("=" * 35)
    print("       SIMPLE BANKING SYSTEM")
    print("=" * 35)

    name = input("Enter account holder name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    pin = input("Create a 4-digit PIN: ").strip()
    if len(pin) != 4 or not pin.isdigit():
        print("PIN must contain exactly 4 digits.")
        return

    account = BankAccount(name, pin)
    print("\nAccount created successfully!")

    entered_pin = input("Enter your PIN to log in: ").strip()
    if entered_pin != account.pin:
        print("Incorrect PIN. Access denied.")
        return

    print(f"\nWelcome, {account.name}!")

    while True:
        print("\n===== BANK MENU =====")
        print("1. Deposit money")
        print("2. Withdraw money")
        print("3. Check balance")
        print("4. Transaction history")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice in ["1", "2"]:
            try:
                amount = float(input("Enter amount (Rs.): "))
                if choice == "1":
                    account.deposit(amount)
                else:
                    account.withdraw(amount)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            account.show_balance()

        elif choice == "4":
            account.show_transactions()

        elif choice == "5":
            print("Thank you for using Simple Banking System!")
            break

        else:
            print("Invalid choice. Please select 1 to 5.")


if __name__ == "__main__":
    main()
