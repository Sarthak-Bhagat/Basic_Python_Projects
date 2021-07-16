"""Caclculate compound interst from a given prinipal, time, and interest rate."""


def compound_interest(principal, rate, time, number):
    """Calculate compund interest."""
    amount = principal * pow(1 + (rate / number), number * time)
    return amount


def main():
    """Take input and outputs answer."""
    principal = float(input("Principal amount: "))
    rate = float(input("Interest rate: "))
    time = float(input("Number of Years: "))
    number = float(input("Number of times interest compunded per year: "))

    rate = rate / 100

    amount = compound_interest(principal, rate, time, number)
    compund_interest = amount - principal

    print(f"Compound interest = {compund_interest:.2f}")
    print(f"Total amount = {amount:.2f}")


if __name__ == "__main__":
    main()
