'''
Created on 17 Nov, 2014

@author: z0037v8z
'''

class LogisticRegression(object):
    def __init__(self):
        pass
    
    def apply(self, dataset, learningRate=0.01):
        # h(x) = g(Q`x)
        # g(z_ = 1/(1+e^(-z))
        q0 = 0.0;
        q1 = 0.0;
        
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
            q0 = q0 - learningRate * derivative0
            q1 = q1 - learningRate * derivative1
            if(abs(cost - lastCost) < 0.001):
                print("Found! q0=" + str(q0) + ", q1=" + str(q1) + ",cost=" + str(cost) + ".")
                break
            else:
                print("Continue! q0=" + str(q0) + ", q1=" + str(q1) + ",cost=" + str((int)(cost)) + ".")
                #input("Next:")

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
algo = LinearRegression()
algo.apply(dataset)
