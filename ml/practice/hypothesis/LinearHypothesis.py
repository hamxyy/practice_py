'''
Created on 2 Dec, 2014

@author: z0037v8z
'''

class LinearHypothesis(object):
    
    parameters = []
    
    def __init__(self):
        pass
    
    def prepare(self, training_set):
        self.parameters = [0 for i in range(0, len(training_set[0]))]
    
    def _apply(self, training_data):
        result = 0
        for i in range(0, len(self.parameters)):
            result += self.parameters[i] * training_data[i]
        return result
    
    def cost(self, training_sample):
        return (self._difference(training_sample)) ** 2 / 2
    
    def derivative(self, training_data, which):
        return training_data[which] * (self._difference(training_data))
    
    def _difference(self, training_data):
        return self._apply(training_data) - training_data[-1]
    
    def description(self):
        desc = "f(x) = "
        i = 0
        for param in self.parameters:
            desc += str(round(param, 1)) + "*x" + str(i) + " + "
            i += 1
        desc = desc.strip().strip("+")
        print(desc)
