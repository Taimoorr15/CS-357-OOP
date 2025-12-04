class Cashier:
    def __init__(self, total_amount, cash_paid):
        if not isinstance(total_amount, int) or not isinstance(cash_paid, int):
            raise TypeError("total amount and cash paid can only be integers!")
        if total_amount < 0 or cash_paid < 0:
            raise ValueError("Total amount and cash paid cannot be lesser than zero!")
        self.total_amount = total_amount
        self.cash_paid = cash_paid

    def change(self):
        change_amount = self.cash_paid - self.total_amount
        if change_amount < 0:
            raise ValueError("Insufficient cash paid!.")
        if change_amount == 0:
            print("No change to givee!.")
            return {}, True

        print(f"The change to be given is: {change_amount}!")
        rupees = [5000, 1000, 500, 100, 50, 20, 10, 5, 2, 1]
        change_given = {}

        for note in rupees:  
            if change_amount <= 0:
                break
            count = change_amount // note  # how many notes of this type we need
            if count:
                change_given[note] = count
                print(f"{note} x {count}")
                change_amount -= note * count

        return change_given, True

