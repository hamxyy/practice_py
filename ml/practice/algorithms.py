'''
Created on 2014Äê11ÔÂ30ÈÕ

@author: Owner
'''
def gradient_descent(dataset, count_parameters, calc_derivatives, learning_rate=0.01):
    # h(x) = g(Q`x)
    # g(z_ = 1/(1+e^(-z))
    parameters = []
    for i in range(0, count_parameters):
        count_parameters[i] = 0.0
    q0 = parameters[0]
    q1 = parameters[1]
    
    derivative = []
    derivative[0] = lambda params, x, y: params[0] + params[1] * x - y
    derivative[1] = lambda params, x, y: (params[0] + params[1] * x - y) * x
    
    # calculation
    derivative0 = 0.0;
    derivative1 = 0.0;
    cost = 0.0
    lastCost = cost
    m = len(dataset)
    while(True):
        for pair in dataset:
            x = pair[0]
            y = pair[1]
            derivative0 += q0 + q1 * x - y
            derivative1 += (q0 + q1 * x - y) * x
            cost += (q0 + q1 * x - y) * (q0 + q1 * x - y)
        derivative0 = derivative0 / m
        derivative1 = derivative1 / m
        cost = cost / m
        q0 = q0 - learning_rate * derivative0
        q1 = q1 - learning_rate * derivative1
        if(abs(cost - lastCost) < 0.001):
            print("Found! q0=" + str(q0) + ", q1=" + str(q1) + ",cost=" + str(cost) + ".")
            return parameters
        else:
            print("Continue! q0=" + str(q0) + ", q1=" + str(q1) + ",cost=" + str((int)(cost)) + ".")
            # input("Next:")
            
def linear_regression(dataset):
    
    return

dataset = [
    [1, 200],
    [2, 300],
    [3, 400],
    [4, 500],
    [5, 600],
    [6, 700],
    [7, 800],
    [8, 900],
]
linear_regression(dataset)
