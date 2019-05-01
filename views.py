count_congress = 0
count_bjp = 0
count_jds = 0


def add_vote_congress():
	global count_congress
	count_congress += 1
	print(count_congress)

def add_vote_bjp():
	global count_bjp
	count_bjp += 1
	print(count_bjp)
	
def add_vote_jds():
	global count_jds
	count_jds += 1
	print(count_jds)

def get_result():
	global count_congress,count_bjp,count_jds
	total = count_congress+count_bjp+count_jds
	congress_count = (count_congress*100)/total
	bjp_count = (count_bjp*100)/total
	jds_count = (count_jds*100)/total
	print("Congress:{} BJP:{} JDS:{}".format(congress_count,bjp_count,jds_count))

	result_list=[congress_count,bjp_count,jds_count]

	return result_list