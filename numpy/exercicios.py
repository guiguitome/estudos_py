import numpy as np

# Básico
# 1. Crie um array de 10 zeros.
zero = np.zeros(10)
print(zero)

# 2. Crie um array de 10 uns
um = np.ones(10)
print(um)

# 3. Crie um array de inteiros de 10 até 50 ERREI
arr = np.arange(10, 50) 
print(arr)

# 4. Crie uma matriz identidade de dimensão 5. ERREI
# five_dim = np.zeros(shape= (3,5,6,7,8))
# print(five_dim)

# 5. Gere 10 números aleatórios entre 0 e 1 com np.random.rand. ERREI
rng = np.random.default_rng()
random = rng.integers(low=0, high=1, size=10, endpoint=True)
print(random)

#refazendo os errados:
# 3
arr_int = np.arange(10,51)
print(arr_int)

# 4 
iden = np.eye(5)
print(iden)

#5 
random = np.random.rand(10)
print(random)