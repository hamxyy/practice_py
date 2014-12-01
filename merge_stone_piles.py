score = 0

def merge_stone_piles(stonepiles):
	if(len(stonepiles)==1):
		finish()
		return
	least_stones_2p = stonepiles[0] + stonepiles[1]
	index_least_stones_2p = 0
	temp = 0
	for n in range(0, len(stonepiles)-1):
		temp = stonepiles[n] + stonepiles[n+1]
		if(temp < least_stones_2p):
			least_stones_2p = temp
			index_least_stones_2p = n
	merge_2_piles(stonepiles, index_least_stones_2p)
	merge_stone_piles(stonepiles)

def merge_2_piles(stonepiles, first_index):
	global score
	#print("Merge " + str(first_index) + " and " + str(first_index + 1) + " out of " + str(stonepiles))
	first = stonepiles.pop(first_index)
	second = stonepiles.pop(first_index)
	score = score + first + second
	stonepiles.insert(first_index, first + second)
	
def finish():
	global score
	#print("Completed!")
	#print("Score = " + str(score))
	print(str(score))
	
merge_stone_piles([31,24,121,3,51,3,123,412,312])