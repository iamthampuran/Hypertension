import numpy as np

# Define the input and target data
X = np.array([[-1, -1], [-1, 1], [1, -1], [1, 1]])
T = np.array([-1, 1, -1, -1])

# Define the initial weights and learning rate
w = np.array([0.2, -0.1])
alpha = 0.2

# Define the Adaline function
def adaline(x, w):
    y_in = np.dot(x, w)
    return np.where(y_in >= 0, 1, -1)

# Train the Adaline network for 2 epochs
for epoch in range(2):
    print("Epoch", epoch+1)
    for i in range(len(X)):
        x = X[i]
        t = T[i]
        y = adaline(x, w)
        error = t - y
        delta_w = alpha * error * x
        w += delta_w
        print("Input:", x, "Target:", t, "Output:", y, "Weights:", w)
