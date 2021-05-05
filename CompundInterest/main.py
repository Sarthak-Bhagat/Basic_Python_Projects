def compound_interest(principal, rate, time, number):
    amount = principal * pow( 1+(rate/number), number*time)
    return amount;

def main():
    principal = float(input('Principal amount: '))
    rate = float(input('Interest rate: '))
    time = float(input('Number of Years: '))
    number = float(input('Number of times interest compunded per year: '))

    rate = rate/100

    amount = compound_interest(principal, rate, time, number)
    ci = amount - principal

    print(f'Compound interest = {ci:.2f}')
    print(f'Total amount = {amount:.2f}')


if __name__ == "__main__":
    main() 
