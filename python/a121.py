from sympy import primerange

start_end = str(input())
start_end = start_end.split(" ")
start = int(start_end[0])
end = int(start_end[1])

primes = list(primerange(start, end))

print(len(primes))