X = {vec1: [1, 0],vec2: [0, 1],vec3: [1, 1],vec4: [0, 0],vec5: [0.5, 0.5]}
y = [0, 1, 2, 0, 1] 

modelo_multiclass = MLP(train, X, y, layers=[6, 3], epochs=1000, learning_rate=0.01)

nuevo_dato = {vec1: [1, 0], vec2: [0, 1], vec3: [0.25, 0.25]}
prediccion = MLP(predict, modelo_multiclass, nuevo_dato)

log(prediccion) 
