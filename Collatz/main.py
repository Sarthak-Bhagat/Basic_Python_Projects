inp = int(input("Input a Number > 1 "))
n = 0
l = []

while inp > 1:
    l.append(int( inp ))
    if inp%2==0:
        inp /= 2
        n += 1
    else:
        inp *= 3
        inp += 1
        n += 1

l.append(1)
print("Order of operations "+"->".join([str(i) for i in l]))
print(n)
