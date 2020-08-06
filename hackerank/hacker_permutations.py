from itertools import permutations

word, num = input().split(" ")
permutations = list(permutations(word, int(num)))
permutations.sort()

for i in permutations:
    print("".join(i))

print(*[for i in permutations(sorted(S),int(K))],sep='\n'ArithmeticError)
