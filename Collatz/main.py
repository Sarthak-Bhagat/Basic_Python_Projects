inp = int(input("Input a Number > 1 "))
N = 0
lst = []

while inp > 1:
    lst.append(int(inp))
    if inp % 2 == 0:
        inp /= 2
        N += 1
    else:
        inp *= 3
        inp += 1
        N += 1

lst.append(1)
print("Order of operations "+"->".join([str(i) for i in lst]))
print(N)
