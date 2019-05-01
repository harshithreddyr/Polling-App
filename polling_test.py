congress = 0
bjp = 0
jds = 0


def vote_cong():
	global congress
	congress += 1
	return congress

def vote_bjp():
	global bjp
	bjp += 1
	return bjp

def vote_jds():
	global jds
	jds += 1
	return jds

def calculate_result():
	global congress,jds,bjp
	total = congress+jds+bjp
	cong_per = (congress*100)/total
	bjp_per = (bjp*100)/total
	jds_per = (jds*100)/total
	print("Congress:{} BJP:{} JDS:{}".format(cong_per,bjp_per,jds_per))


while True:
	print('congress:',congress)
	print('BJP:',bjp)
	print('JDS:',jds)
	choice = int(input("\nWho do you want to Vote:\n1.Congress\n2.BJP\n3.JD\n4.Calculate Results\n"))
	if choice == 1:
		vote_cong()
	elif choice == 2:
		vote_bjp()
	elif choice == 3:
		vote_jds()
	elif choice == 4:
		calculate_result()
	else:
		print("Invalid choice")
		break	



