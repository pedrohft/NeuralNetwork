import numpy as np 

def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))

def sigmoidDerivada(sig):
    return sig * (1 - sig)

# a = sigmoid(0.5)
# b = sigmoidDerivada(a)
# print(a)
# print(b)

entradas = np.array([[0,0], #Operador XOR
                     [0,1],
                     [1,0],
                     [1,1]])

saidas = np.array([[0], [1], [1], [0]]) #Operador XOR

# pesos0 = np.array([[-0.424, -0.740, -0.961],
#                     [0.358, -0.577, -0.469]]) #pesos da camada de entrada para a oculta

# pesos1 = np.array([[-0.017], [-0.893], [0.148]]) #pesos da camada oculta para a saida


pesos0 = 2*np.random.random((2,3)) - 1
pesos1 = 2*np.random.random((3,1)) - 1

print(pesos0)
print(pesos1)
epocas = 1000000
taxaAprendizagem = 0.6
momento = 1

for j in range(epocas):
    camadaEntrada = entradas
    somaSinapse0 = np.dot(camadaEntrada, pesos0)
    camadaOculta = sigmoid(somaSinapse0)

    somaSinape1 = np.dot(camadaOculta, pesos1)
    camadaSaida = sigmoid(somaSinape1)

    erroCamadaSaida = saidas - camadaSaida
    mediaAbsoluta = np.mean(np.abs(erroCamadaSaida))
    print("Erro: " + str(mediaAbsoluta))

    derivadaSaida = sigmoidDerivada(camadaSaida)
    deltaSaida = erroCamadaSaida * derivadaSaida       

    pesos1Transposta = pesos1.T
    deltaSaidaXPeso = deltaSaida.dot(pesos1Transposta)
    deltaCamadaOculta = deltaSaidaXPeso * sigmoidDerivada(camadaOculta)

    camadaOcultaTransposta = camadaOculta.T 
    pesosNovo1 = camadaOcultaTransposta.dot(deltaSaida)
    pesos1 = (pesos1 * momento) + (pesosNovo1 * taxaAprendizagem) #backpropagation

    camadaEntradaTransposta = camadaEntrada.T 
    pesosNovo0 = camadaEntradaTransposta.dot(deltaCamadaOculta)
    pesos0 = (pesos0 * momento) +  (pesosNovo0 * taxaAprendizagem)

# print(pesos0)