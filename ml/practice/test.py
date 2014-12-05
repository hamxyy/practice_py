'''
Created on 2 Dec, 2014

@author: z0037v8z
'''
from algorithms import gradient_descent
from hypothesis.LogisticHypothesis import LogisticHypothesis

# training_set = [
#     [1, 5, 205],
#     [2, 4, 304],
#     [3, 3, 403],
#     [4, 2, 502],
#     [5, 1, 601],
#     [6, -10, 690],
#     [7, -10, 790],
#     [8, -1, 899],
# ]

training_set = [
    [0,1,1,1,1],
    [1,1,0,1,0],
    [0,1,1,0,1],
    [0,0,0,0,0],
    [1,1,1,1,0],
    [1,0,0,0,1],
    [1,0,1,1,0],
    [1,1,1,0,0],
    [0,0,1,0,1],
    [0,1,0,1,0],
    [1,0,1,1,1],
    [0,1,1,0,0],
    [1,0,0,1,1],
]

hypo = LogisticHypothesis();
gradient_descent(hypothesis=hypo,
                 training_set=training_set,
                 convergent_ratio=0.001)
