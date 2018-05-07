from CouplingsFitterHL import *

f=CouplingsFitter()


###Here add the Parameters of interest with a reasonable range
##############################################################
f.addPOI('W','W',-0.05,0.05)
f.addPOI('b','b',-0.1,0.1)
#is this a good range?
f.addPOI('width','width',-0.8,0.8)


###Here add the constraints 'name','formula','dependents',mean value ,error 
################################################
f.addConstraint('Whbb','(1+W)*(1+W)*(1+b)*(1+b)/(1+width)','W,b,width',1,0.002*0.95)
f.addConstraint('tot','width','width',1,0.5)


################################################
f.fit()
#c,cprime,obj = f.createSummary()
c = f.createSummary()
c.Draw()
#cprime.Draw()
