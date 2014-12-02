'''
Created on 2 Dec, 2014

@author: z0037v8z
'''
from Hypothesis import LinearHypothesis
from algorithms import gradient_descent

training_set = [
    [1, 200],
    [2, 300],
    [3, 400],
    [4, 500],
    [5, 600],
    [6, 700],
    [7, 800],
    [8, 900],
]

def multiply(list1, list2, length):
    result = 0
    for i in range(0, length):
        result += list1[i] * list2[i]
    return result

derivatives = [
    lambda params, data: multiply(params, data, len(params)) - data[len(params)],
    lambda params, data: (params[0] + params[1] * data[1] - data[2]) * data[1]
]
desc = lambda params: print("f(x) = " + str(round(params[0], 2)) + " + " + str(round(params[1], 2)) + " * x")
cost_func = lambda params, data: (params[0] + params[1] * data[1] - data[2]) ** 2
hypo = LinearHypothesis(derivatives=derivatives,
                        parameters=[0, 0],
                        cost=cost_func,
                        desc=desc);

gradient_descent(hypo, training_set)
