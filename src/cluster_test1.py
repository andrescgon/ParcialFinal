X = {vec1: [1, 2],vec2: [1.5, 1.8],vec3: [5, 8],vec4: [8, 8],vec5: [1, 0.6],vec6: [9, 11]}

modelo_kmeans = cluster(kmeans, X, {n_clusters: 2, max_iter: 100, tolerance: 0.001})

log(modelo_kmeans.get_clusters()) 

nuevo_dato = {vec1: [3, 3]}
resultado = cluster_predict(modelo_kmeans, nuevo_dato)

log(resultado)
