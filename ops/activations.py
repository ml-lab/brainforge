import numpy as np


class ActivationFunction:

    type = ""

    def __call__(self, Z: np.ndarray) -> np.ndarray:
        raise NotImplementedError

    def __str__(self):
        return self.type

    def derivative(self, Z: np.ndarray) -> np.ndarray:
        raise NotImplementedError


class Sigmoid(ActivationFunction):

    type = "sigmoid"

    def __call__(self, Z: np.ndarray) -> np.ndarray:
        return np.divide(1.0, np.add(1, np.exp(-Z)))

    def derivative(self, A) -> np.ndarray:
        return A * np.subtract(1.0, A)


class Tanh(ActivationFunction):

    type = "tanh"

    def __call__(self, Z) -> np.ndarray:
        return np.tanh(Z)

    def derivative(self, A) -> np.ndarray:
        return np.subtract(1.0, np.square(A))


class Linear(ActivationFunction):

    type = "linear"

    def __call__(self, Z) -> np.ndarray:
        return Z

    def derivative(self, Z) -> np.ndarray:
        return np.ones_like(Z)


class ReLU(ActivationFunction):

    type = "relu"

    def __call__(self, Z) -> np.ndarray:
        return np.maximum(0.0, Z)

    def derivative(self, A) -> np.ndarray:
        d = np.ones_like(A)
        d[A <= 0.] = 0.
        return d


class SoftMax(ActivationFunction):

    type = "softmax"

    def __call__(self, Z) -> np.ndarray:
        # nZ = Z - np.max(Z)
        eZ = np.exp(Z)
        return eZ / np.sum(eZ, axis=1, keepdims=True)

    def derivative(self, A: np.ndarray) -> np.ndarray:
        return 1.

    def true_derivative(self, A: np.ndarray):
        # TODO: test this with numerical gradient testing!
        I = np.eye(A.shape[1])
        idx, idy = np.diag_indices(I)
        return A * (A[..., None] - I[None, ...])[:, idx, idy]


act_fns = {key.lower(): cls for key, cls in locals().items() if "Function" not in key}
