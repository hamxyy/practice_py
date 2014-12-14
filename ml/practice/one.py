from math import log

class LinearHypothesis(object):
    def prepare(self, training_set):
        self.parameters = [0] * (len(training_set[0]))
    
    def _apply(self, training_data):
        result = 0
        for i in range(0, len(self.parameters)):
            result += self.parameters[i] * training_data[i]
        return result
    
    def cost(self, training_sample):
        return (self._error(training_sample)) ** 2 / 2
    
    def derivative(self, training_data, which):
        return training_data[which] * (self._error(training_data))
    
    def _error(self, training_data):
        return self._apply(training_data) - training_data[-1]

    def description(self):
        desc = "f(x) = "
        i = 0
        for param in self.parameters:
            desc += str(round(param, 1)) + "*x" + str(i) + " + "
            i += 1
        desc = desc[0:-2]
        print(desc)

class LogisticHypothesis(object):
    def prepare(self, training_set):
        self.parameters = [0] * (len(training_set[0]))
    
    def _apply(self, training_data):
        result = 0
        for i in range(0, len(self.parameters)):
            result += self.parameters[i] * training_data[i]
        return result
    
    def cost(self, training_data):
        y = training_data[-1]
        result = self._apply(training_data) + 0.0000001  # just to cater to log function when result = 0
        return (-y) * log(result) - (1 - y) * log(1 - result)
    
    def derivative(self, training_data, which):
        return training_data[which] * (self._error(training_data))
    
    def _error(self, training_data):
        return self._apply(training_data) - training_data[-1]

    def description(self):
        desc = "f(x) = g("
        i = 0
        for param in self.parameters:
            desc += str(round(param, 1)) + "*x" + str(i) + " + "
            i += 1
        desc = desc[0:-2] + ")"
        print(desc)

def gradient_descent(hypothesis, training_set, learning_rate=0.01, convergent_criteria=0.005):
    hypothesis.prepare(training_set)
    for training_data in training_set:
        training_data.insert(0, 1)
    # calculation
    offsets = [0] * len(hypothesis.parameters)
    cur_cost, last_cost = 0, 0
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
        if(abs(cur_cost - last_cost) < convergent_criteria):
            hypothesis.description()
            break
        last_cost = cur_cost

# Actually generated using formula f(x) = x1*5 + x2*5 - x3*10 + x4*2
training_set = [[50, 50, 20, 100, 500], [70, 60, 22, 101, 632], [65, 40, 20, 110, 545], [81, 60, 19, 99, 713], [62, 50, 19, 102, 574], [73, 50, 20, 103, 621], [68, 40, 18, 105, 570], [62, 70, 23, 104, 638], [75, 40, 22, 102, 559], [79, 30, 24, 110, 525], ]
hypo = LinearHypothesis();
gradient_descent(hypothesis=hypo,
                 training_set=training_set,
                 learning_rate=0.0001,
                 convergent_criteria=0.05)
# Result: f(x) = 0.0*x0 + 4.7*x1 + 4.8*x2 + -2.7*x3 + 0.8*x4 
