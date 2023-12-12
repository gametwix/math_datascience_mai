import numpy as np
from abc import ABC, abstractmethod

class Regression(ABC):
    @abstractmethod
    def __init__(self, X, y):
        ...
        
    @abstractmethod
    def __call__(self):
        ...
        
class LinearRegression(Regression):
    def __init__(self, X, y):
        a = [[np.sum(x**2 for x in X), sum(X)],[sum(X), len(X)]]
        b = 
        self.b0 = 0
        self.b1 = 0
        