def Fizzzzzzzzzzzzz(n):
    return ((n%3==0)*"Fizz" + (n%5==0)*"Buzz") or n

def Buzzzzzzzzzzzzz():
    return("\n".join([str(Fizzzzzzzzzzzzz(i)) for i in range(100001)]))

if __name__ == "__main__":
    print(Buzzzzzzzzzzzzz()) 
