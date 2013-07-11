def getGreatest(input):
	p = 1
	i = 2
	while (i < input):
		if ((i**p) == input):
			return p
 		elif ((i**p) > input):
			i += 1
			p = 1
		else: 
			p+=1
	return p # in the case that i gets larger than input
print getGreatest(1073741823)