import numpy as np


class ClusteringModel:
    def __init__(self, method, params=None):
        self.method = method.lower()
        self.params = params if params else {}
        self.centroids = None
        self.labels = None

    def fit(self, X_obj):
        X = self._convert_object_to_array(X_obj)

        if self.method == 'kmeans':
            self._fit_kmeans(X)
        else:
            raise ValueError(f"Método de clustering '{self.method}' no soportado")
        return self

    def predict(self, X_obj):
        if self.centroids is None:
            raise ValueError("El modelo no ha sido entrenado aún")

        X = self._convert_object_to_array(X_obj)
        return self._assign_clusters(X).tolist()

    def get_clusters(self):
        return self.labels.tolist() if self.labels is not None else None

    def _fit_kmeans(self, X):
        n_clusters = self.params.get('n_clusters', 2)
        max_iter = self.params.get('max_iter', 100)
        tolerance = self.params.get('tolerance', 1e-4)

        # Inicialización aleatoria de centroides
        np.random.seed(42)  # Para reproducibilidad
        random_indices = np.random.choice(len(X), size=n_clusters, replace=False)
        self.centroids = X[random_indices]

        for _ in range(max_iter):
            # Asignar clusters
            labels = self._assign_clusters(X)

            # Calcular nuevos centroides
            new_centroids = np.array([
                X[labels == cluster].mean(axis=0) if len(X[labels == cluster]) > 0 else self.centroids[cluster]
                for cluster in range(n_clusters)
            ])

            # Comprobar convergencia
            if np.linalg.norm(new_centroids - self.centroids) < tolerance:
                break

            self.centroids = new_centroids

        self.labels = labels

    def _assign_clusters(self, X):
        distances = np.linalg.norm(X[:, np.newaxis] - self.centroids, axis=2)
        return np.argmin(distances, axis=1)

    def _convert_object_to_array(self, X_obj):
        """Convierte el objeto de tipo {vec1: val1, vec2: val2} a array numpy"""
        if not X_obj:
            raise ValueError("Empty input object")

        X_list = []
        for key in sorted(X_obj.keys()):
            value = self._get_value(X_obj[key])
            if isinstance(value, (list, tuple)):
                X_list.append([float(self._get_value(v)) for v in value])
            else:
                X_list.append([float(value)])
        return np.array(X_list)

    def _get_value(self, x):
        """Extrae el valor numérico de una variable TLON o retorna el valor si ya es numérico"""
        if hasattr(x, 'value'):
            return x.value
        return x
