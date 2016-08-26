#7.2,7.3
def count_letters(words='',ch='',a=0):
	count=0
	for char in words[a:]:
		print (char)
		if char==ch:
			count+=1
		
	return count
#