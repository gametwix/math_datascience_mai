import numpy as np

def quadratic(A, b, c, x):
    return np.dot(np.dot(A, x), x) + np.dot(b, x) + c

def quadratic_gradient(A, b, x):
    return 2 * np.dot(A, x) + b

def get_norm(type_norm="max", l = 1):
    if type_norm == "max":
        return lambda x: np.max(np.absolute(x))
    elif type_norm == "mae":
        return lambda x: np.sum(np.absolute(x))
    elif type_norm == "mse":
        return lambda vector: sum(x**(2*l) for x in vector)**(1/(2*l))

x = np.array([0, 0])
A = np.array([[1, 0], [0, 1]])
b = np.array([-2 , -4])
c = 5
lr = 0.1
x2 = x - lr*quadratic_gradient(A,b,x)
epoch = 0
distance = x2 - x
norm = get_norm("mae")
print(f"Epoch {epoch}: x={x2}, f(x)={quadratic(A, b, c, x2)} norm={norm(distance)}")
while norm(distance) > 10**(-5):
    epoch += 1
    x = x2
    x2 = x - lr*quadratic_gradient(A,b,x)
    distance = x2 - x
    print(f"Epoch {epoch}: x={x2}, f(x)={quadratic(A, b, c, x2)} norm={norm(distance)}")

gradient = quadratic_gradient(A, b, x)
print(x2)

