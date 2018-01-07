def reciprocal(num):
	try:
		r = 1.0/num
	except:
		print ('Exception caught!')
		return
	return r

print (reciprocal(10))
print (reciprocal(0))
