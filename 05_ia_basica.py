from sklearn.tree import DecisionTreeClassifier

# Dados de treinamento: altura (m), peso (kg)

X = [[1.2, 25], [1.5, 50], [1.0, 20], [1.8, 70], [1.75, 65]]
y = [0, 1, 0, 1, 1] # 0 = criança, 1 = adulto

# Treinamento do modelo
modelo = DecisionTreeClassifier()
modelo.fit(X, y)

# Teste do modelo
# A altura de 1.3 m e peso de 30 kg deve ser classificada
# como criança (0) ou adulto (1)
# A altura de 1.3 m e peso de 30 kg é mais provável de
# ser classificada como criança (0) com base nos dados de treinamento
# Nova pessoa a ser classificada
novo = [[1.3, 30]]
resultado = modelo.predict(novo)
print('É adulto' if resultado[0] == 1 else 'É criança')
