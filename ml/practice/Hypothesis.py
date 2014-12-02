'''
Created on 2 Dec, 2014

@author: z0037v8z
'''

class LinearHypothesis(object):
    
    def __init__(self, derivatives, parameters, cost, desc):
        self.derivatives = derivatives
        self.parameters = parameters
        self._cost = cost
        self.desc = desc
        pass
    
    def calc(self, training_set):
        result = 0
        for i in range(0, len(self.parameters)):
            result += self.parameters[i] * training_set[i]
        return result
    
    def cost(self, training_sample):
        return self._cost(self.parameters, training_sample)
    
    def derivative(self, training_data, which):
        #print(training_data)
        #print(which)
        #print(self.parameters)
        return self.derivatives[which](self.parameters, training_data);
    
    def description(self):
        self.desc(self.parameters)