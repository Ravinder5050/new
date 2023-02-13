def cuberoot(x,debug=False,specialcase=True):

	from numpy import nan
	
	if x==0.:
		return 0.
	elif x<0.:
		print("An error has occured since if you gave negative value for x which does not have a real square root")
		return nan
	if specialcase:
		if x==0.:
			return 0.
		elif x<0.:
			print("An error has occured since you have pass a negative value for" 
		   "x which does not have a real square root")
			return nan
	assert x>0., "Input is not recognised"
	s=1.
	kmax=100
	tol=1.0e-14
	for k in range(kmax):
		print("At Iteration number %s, s= %s" %(k,s))
		s0 =s
		s =1/3*(2*s+x/s**2)
		delta_s= s-s0
		if(abs(delta_s/x))<tol:
			break
	print("After %s iterations, s=%20.15f" %(k+1,s))
