'''
Created on 2014-12-02

@author: z0037v8z
'''

def gradient_descent(hypothesis, training_set, learning_rate=0.01):
    for training_data in training_set:
        training_data.insert(0, 1)
    # calculation
    offsets = []
    for i in range(0, len(hypothesis.parameters)):
        offsets.append(0)

    cur_cost = 0.0
    lastCost = cur_cost
    m = len(training_set)
    while(True):
        for training_sample in training_set:
            for i in range(0, len(offsets)):
                offsets[i] += hypothesis.derivative(training_sample, i)
            cur_cost += hypothesis.cost(training_sample)
        for i in range(0, len(offsets)):
            offsets[i] = offsets[i] / m
        cur_cost = cur_cost / m
        for i in range(0, len(offsets)):
            hypothesis.parameters[i] = hypothesis.parameters[i] - learning_rate * offsets[i]
        if(abs(cur_cost - lastCost) < 0.001):
            hypothesis.description()
            break
        #else:
        #    hypothesis.description()
        #    input("Next:")
