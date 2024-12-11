X = {vec1: [1, 2], vec2: [4, 5], vec3: [7, 8]}
y = [0, 1, 1]

model = MLP(train, X, y, layers=[4], epochs=1000, learning_rate=0.01)

nuevo_dato = {vec1: [3, 4]}
prediccion = MLP(predict, model, nuevo_dato)
log(prediccion)
