#creating tuple
fruit=('apple','banana','grape','orange')
a,b,c,d=fruit
#slice: tuple[m:n],m<=,<n
print fruit[3:]
print a,b,d
#two-dimensional tuple
date=((06,02),(06,17))
print date[0][1]
#range([start,]stop[,step])
even=range(0,9,2)
odd=range(1,9,2)
print even
print odd
#len()
print len(even)
print len(odd)
#map(function,sequenece[,sequenece])
r=map(None,even)
for i in r:
	print i
