from sympy import primefactors


inp = int(input("Which number do you want the prime factors of? "))
print(f"The factors of {inp} are " + ", ".join([str(i) for i in primefactors(inp)]))
