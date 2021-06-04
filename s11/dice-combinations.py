#!/usr/bin/python3.7

# https://cses.fi/problemset/task/1633

# dp[n]: cantidad de formas de sumar 'n' tirando cualquier cantidad de dados.
# como calcular dp[n] en función de la otra información procesada?

# tengo una suma x, el dado me da un valor k
# mi nueva suma va a ser x + k
# dp[x+k] += dp[x]

'''
# solucion recursiva
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)

n = int(input())
mod = (10**9) + 7

dp = [-1] * (n+1)

def solve(x):
    # tengo una suma x
    # el ultimo dado que tiré me dio un valor 'i'
    # entonces la suma que tenía antes del ultimo dado
    # era x-i
    # entonces a mi cantidad de formas, debo sumarle dp[x-i]
    if x < 0: return 0
    if x == 0: return 1
    if dp[x] != -1: return dp[x]

    ways = 0
    for i in range(1, 7):
        ways += solve(x-i)
        ways %= mod
    dp[x] = ways
    return ways

print(solve(n))
'''

n = int(input())
mod = 10**9 + 7
# Solución iterativa
dp = [0] * (n+8)
dp[0] = 1

for x in range(n):
    for k in range(1, 7):
        dp[x+k] += dp[x]
        dp[x+k] %= mod
print(dp[n])

