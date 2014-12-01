import math

TIME_LIFT_GO_1_LEVEL = 4
TIME_LIFT_LAUNCH = 10
TIME_MAN_GO_1_LEVEL = 20

class Calculator(object):

	def find_from_all(self, dests):
		least_route = {}
		best_stops = None
		for stops in self.enumerate_all_possibilities(dests):
			if(dests[len(dests)-1] not in stops): #should at least stop at the last stop
				continue
			route = self.calculate_latest_time(dests, stops)
			if("time" not in least_route or route["time"] < least_route["time"]):
				least_route = route
				best_stops = stops
		return {"stops":best_stops, "lastest_route":least_route}
	
	def enumerate_all_possibilities(self, dests):
		result = []
		mask = 1
		while(mask < 2**len(dests)):
			mask_str = bin_to_str(mask, len(dests))
			stops = []
			for i in range(0, len(mask_str)):
				if(mask_str[i]=='1'):
					stops.append(dests[i])
			result.append(stops)
			mask += 1
		return result

	'''
			dests: [4,7,10,40,100,231]
			stops: [4,  10,       231]
		return: {"stop":s, "time":t, "dest":dest}
	'''
	def calculate_latest_time(self, dests, stops):
		if(dests[len(dests)-1] not in stops):
			print("This case doesn't make sense as the last stop {0} is not included in the stops({1}).".format(dests[len(dests)-1], stops))
			return
		max_route = {"stop":None, "time":0}
		for dest in dests:
			route = self.find_fastest_route(dest, stops)
			stop = route["stop"]
			time = route["time"]
			#print("max_route is " + str(max_route))
			#print("Route for " + str(dest) + " is " + str(route))
			if(time > max_route["time"]):
				max_route = route
				max_route["dest"] = dest
		return max_route
			
	def find_fastest_route(self, dest, stops):
		if(dest in stops):
			return {"stop":dest, "time":self.lift_time(dest, stops)}
		pre = stops[0]
		after = stops[0]
		for stop in stops:
			if(stop < dest):
				pre = stop
			if(stop > dest):
				after = stop
				break
		pre_time = self.walk_time(pre, dest) # alight before
		after_time = self.walk_time(after, dest) + self.lift_time(after, stops) # alight at next stop
		initial_time = self.lift_time(pre, stops)
		if(pre_time < after_time):
			return {"stop":pre, "time":pre_time}
		else:
			return {"stop":after, "time":after_time}
	
	'''
		return the time it takes for the lift to go to dest,
		time for stops is included.
	'''
	def lift_time(self, dest, stops):
		stops_before_dest = 0
		for stop in stops:
			if(dest>stop and stop>1):
				stops_before_dest += 1
		return (dest-1)*TIME_LIFT_GO_1_LEVEL + stops_before_dest*TIME_LIFT_LAUNCH
	
	def walk_time(self, start, stop):
		return abs(stop - start) * TIME_MAN_GO_1_LEVEL

def bin_to_str(i, lens):
	bin_i = bin(i).replace("0b", "")
	result = bin_i
	for i in range(0, lens-len(bin_i)):
		result = '0' + result
	return result