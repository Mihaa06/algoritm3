n=int(input())
z=0
p=1
while n > 0:
    c= n% 10
    n=int(n/10)
    if c % 3 == 0:
        z=z + p*(9-c)
        p=p*10
        print(z)