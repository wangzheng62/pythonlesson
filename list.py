#creating list
number=[0,1,2,3,4]
#append()
number.append(5)
print number
number.append((6,7))
print number
l=[8,9,10]
number.append(l)
print number
#remove()
number.remove((6,7))
print number
number.remove(l)
print number
#insert(n,object)
number.insert(6,6)
print number
number.insert(8,8)
print number[7]
print number[-3:-1]
#pop()
number.pop()
print number[-3:-1]
#index()
print number.index(5)
print 5 in number
#reverse()
number.reverse()
print number
#sort()
number.sort()
print number
#extend()
number.extend(l)
print number
