'''
author: Zhu Zhong
email: hamxyy@gmail.com
'''

'''
Premises and assumptions:
1. Lift always goes faster than man does.

'''

import lift_quiz_calculator

# Parameters
TIME_LIFT_GO_1_LEVEL = 4
TIME_LIFT_LAUNCH = 10
TIME_MAN_GO_1_LEVEL = 20

def start(dests):
	dests.sort()
	for dest in dests:
		print(dest)

# This is always true in this quiz.
def should_go_by_lift_or_walk_when_lift_has_stopped(current, target):
	return (TIME_LIFT_LAUNCH + calc_time_lift_take_no_stop(current, target)) <= calc_time_man_take(current, target)

def calc_time_lift_take_no_stop(current, target):
	return (target - current) * TIME_LIFT_GO_1_LEVEL
	
def calc_time_man_take(current, target):
	return (target - current) * TIME_MAN_GO_1_LEVEL

def calc_all_possibilities(dests):
	flag_str = ""
	for dest in dests:
		flag_str += "0"
	flag = int(flag_str, 2) 
		
calc_all_possibilities([2,3,101])
