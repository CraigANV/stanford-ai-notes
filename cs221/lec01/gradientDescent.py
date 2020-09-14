points = [(2, 4), (4, 2)]

# Loss function
def F(w):
    return sum((w * x - y)**2 for x, y in points)

# Gradient of the Loss function
def dF(w):
    return sum(2*(w * x - y) * x for x, y in points)

# Gradient descent
w = 0.0  # initial weight
a = 0.01  # learning rate

for t in range(100):
    loss = F(w)
    gradient = dF(w)
    w = w - a * gradient
    print('iteration {}: w = {}, F(w) = {}, dF(w) = {}'.format(t, w, loss, gradient))
