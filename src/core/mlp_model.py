import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

class MLPModel:
    def __init__(self, layers, epochs, learning_rate):
        self.layers = layers
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.weights = []
        self.biases = []
        
    def _get_value(self, x):
        """Extrae el valor numérico de una variable TLON o retorna el valor si ya es numérico"""
        if hasattr(x, 'value'):
            return x.value
        return x

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

    def initialize_network(self, input_size, output_size):
        layer_sizes = [input_size] + self.layers + [output_size]
        for i in range(len(layer_sizes) - 1):
            limit = np.sqrt(6 / (layer_sizes[i] + layer_sizes[i+1]))
            self.weights.append(np.random.uniform(-limit, limit, (layer_sizes[i], layer_sizes[i+1])))
            self.biases.append(np.zeros((1, layer_sizes[i+1])))

    def forward_propagation(self, X):
        self.activations = [X]
        for i in range(len(self.weights)):
            net = np.dot(self.activations[-1], self.weights[i]) + self.biases[i]
            activation = sigmoid(net)
            self.activations.append(activation)
        return self.activations[-1]

    def backpropagation(self, X, y):
        m = X.shape[0]
        output = self.forward_propagation(X)
        error = output - y
        delta = error * sigmoid_derivative(output)
        
        for i in reversed(range(len(self.weights))):
            dW = np.dot(self.activations[i].T, delta) / m
            db = np.sum(delta, axis=0, keepdims=True) / m
            
            self.weights[i] -= self.learning_rate * dW
            self.biases[i] -= self.learning_rate * db
            
            if i > 0:
                delta = np.dot(delta, self.weights[i].T) * sigmoid_derivative(self.activations[i])

    def train(self, X_obj, y):
        # Convertir objeto a array numpy y manejar variables TLON
        X = self._convert_object_to_array(X_obj)
        
        # Convertir y a array numpy y manejar variables TLON
        if isinstance(y, (list, tuple)):
            y = np.array([float(self._get_value(val)) for val in y])
        else:
            y = np.array([float(self._get_value(y))])
        
        # Convertir a formato one-hot
        if len(y.shape) == 1:
            y = y.astype(int)  # Asegurarse de que y sea de tipo entero
            n_classes = len(np.unique(y))
            y_one_hot = np.zeros((len(y), n_classes))
            for i in range(len(y)):
                y_one_hot[i, y[i]] = 1
            y = y_one_hot
        
        # Inicializar red si es necesario
        if not self.weights:
            self.initialize_network(X.shape[1], y.shape[1])
        
        # Entrenamiento
        for _ in range(self.epochs):
            self.backpropagation(X, y)
            
        return self

    def predict(self, X_obj):
        X = self._convert_object_to_array(X_obj)
        predictions = self.forward_propagation(X)
        return np.argmax(predictions, axis=1)
