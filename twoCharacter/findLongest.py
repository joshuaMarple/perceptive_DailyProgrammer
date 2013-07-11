a = ""
b = ""
count = 0
input = "abbbcaccbcabcabccccc"
longest = ""
curLongest = ""
for i in input:
	if a == "":
		a = i
		longest += i
		continue
	if b == "":
		b = i
		longest += i
		continue
	if (i != a or i != b or i == len(input)):
		if longest == a or longest == b:
			longest += i
		if len(longest) >= len(curLongest):
			curLongest = longest
		longestRep = longest.replace(a, "")
		longest = longestRep
		a = b
		b = i
		longest += i
	else:
		longest += i

print curLongest
	


