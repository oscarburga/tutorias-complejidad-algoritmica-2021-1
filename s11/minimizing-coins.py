# Enlace al problema: https://cses.fi/problemset/task/1634/

#!/usr/bin/python3.7

# 
# dp[s] = minima cantidad de monedas necesarias para sumar 's'
# si yo estoy considerando una moneda que vale 'k', 
# entonces yo tengo algunas opciones:
#     * Yo puedo llegar a una suma s + k agregando esta moneda
#     * o puedo simplemente no agregar la moneda y seguir con una suma 's'

# estoy evaluando la moneda 'k' con suma 's': 
#   dp[s+k] = min(dp[s+k], dp[s] + 1)

# X = 10
# S = 7
# K = 5
# dp[0...X]
# dp[S+K] = min(dp[S+K], dp[S] + 1)
# dp[12] = min(dp[12], dp[7] + 1)
# Hay que tener cuidado que S+K <= X

n, x = map(int, input().split())
coins = [int(x) for x in input().split()]

inf = 10**7

dp = [inf] * (x+1)
dp[0] = 0

'''
for k in coins:
    for s in range((x+1) - k):
        dp[s+k] = min(dp[s+k], dp[s] + 1)
'''

for k in coins:
    for s in range(k, x+1):
        dp[s] = min(dp[s], dp[s-k] + 1)

if dp[x] == inf:
    print('-1')
else: 
    print(dp[x])
