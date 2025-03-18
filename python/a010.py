a = int(input())
factors= []
i = 2
while a != 1:
    j = 0
    while a % i == 0:
        j += 1
        a  //= i
    if j > 0:
        if j == 1:
            factors.append(str(i))
        else:
            factors.append(f"{i}^{j}")
    i += 1

print(" * ".join(factors))