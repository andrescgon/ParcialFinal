X = {vec1: [0, 0], vec2: [0, 1], vec3: [1, 0], vec4: [1, 1]}
y = [0, 1, 1, 0] 

modelo_xor = MLP(train, X, y, layers=[4], epochs=5000, learning_rate=0.1)

nuevo_dato = {vec1: [0, 0], vec2: [1, 1], vec3: [1, 0], vec4: [0, 1]}
prediccion = MLP(predict, modelo_xor, nuevo_dato)

log(prediccion) 
