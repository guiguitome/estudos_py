#importação da bilbioteca
import numpy as np

#arrays
a = np.array([1,2,3,4,5,6]) #vetor
print(a)

b = np.array([[1,2,3,4], [5,6,7,8]]) #matriz
print(b)

#np.zeros -> array apenas com zeros
zero = np.zeros((4,4)) #shape seria indicando o formato dela, no caso sendo (4,4) (4 horizontal e 4 vertitcal)
print(zero)

#np.ones -> array apenas com uns
um = np.ones((6,7))
print(um)

#np.empty -> preenche o array com "lixo"
vazio = np.empty((2,2))
print(vazio)

#np.arrange -> array com numéros intervalados
arr = np.arange(2,11,2) #np.arrange(num_começo, num_termina (não conta com ele), passos)
print(arr)

#np.linspace -> arry com numeros espaçados linearmente
linear = np.linspace(0, 10, num=5)
print(linear)

# Descobrindo o tamanho de um array:
print(b.shape) # mostra o formato de um array
print(b.size) # mostra o numéro de dados do array
print(b.ndim) # mostra quantas dimensões tem o array

# reestruturando um array
#np.reshape -> muda o formato do array (porem tem que ter o mesmo numero de elementos)
c = np.array([1,2,3,4,5,6])
d = c.reshape(3, 2)
print(d)

#concatenar arrays
x = np.array([[1,2], [3,4]])
y = np.array([[5,6]])
z = np.concatenate((x,y), axis=0)
print(z)

#consultando itens
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print('++++++++++++')
a_par = a[a%2 == 0]
print(a_par)

#gerando numeros aleatorios
rng = np.random.default_rng()
