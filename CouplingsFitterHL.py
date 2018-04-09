from GenericFitter import *
from math import sqrt
class CouplingsFitter(GenericFitter):
    def __init__(self):
        self.BR=dict()
        self.BR['b'] = 0.577
        self.BR['W'] = 0.215
	#self.BR['width']=0.577+0.215

        super(CouplingsFitter,self).__init__()


    def createPOIs(self,inv = True):
        self.addPOI('W','W',-0.1,0.000001)
        self.addPOI('b')
	self.addPOI('width')

    def createSummary(self):
        #sample the covariance matrix for the width
        ROOT.gStyle.SetOptTitle(0)
        graph = ROOT.TGraphAsymmErrors(len(self.poi)+1)

        for i,poi in enumerate(self.poi):
            graph.SetPoint(i,i+0.5,self.w.var(poi).getVal())
            graph.SetPointError(i,0.0,0.0,-self.w.var(poi).getAsymErrorLo(),self.w.var(poi).getAsymErrorHi())

        print 'Sampling the covariance matrix to propagate error on width'
        #histo=ROOT.TH1F('h','h',1000,0.5,1.5)
        #for i in range(0,10000):
            # this samples the covariance matrix
        #    randomizedPars = self.fitResult.randomizePars()
        #    for j in range(0,randomizedPars.getSize()):
        #        self.w.var(randomizedPars.at(j).GetName()).setVal(randomizedPars.at(j).getVal())
        #    histo.Fill(self.w.function('width').getVal())    
        graph.SetMarkerStyle(20)
        graph.SetLineWidth(3)
        c = ROOT.TCanvas('canvas','')
        c.cd()
        obj=[graph]
        graph.Draw("AP")
        graph.GetYaxis().SetTitle("68% CL on d(A) ")
        graph.GetXaxis().SetNdivisions(0)
        l=ROOT.TLine()
        l.SetLineColor(ROOT.kRed)
        l.SetLineWidth(3)
        l.DrawLine(0.0,0.0,len(self.poi),0)
        obj.append(l)


        #graph.SetPoint(len(self.poi),len(self.poi)+0.5,0.0)
        #graph.SetPointError(len(self.poi),0.0,0.0,histo.GetRMS()/histo.GetMean(),histo.GetRMS()/histo.GetMean())


        for i,label in enumerate(self.poiLabels):
            obj.append(ROOT.TLatex(i+0.5,0.95*graph.GetYaxis().GetXmin(),label))
            obj[-1].Draw()

        print """
###############################################################
###############################################################
###############################################################
                         RESULTS
###############################################################
###############################################################
############################################################### 
              """

        print 'RESULTS FOR THE CONFIDENCE INTERVALS------>'
        for poi,poiLabel in zip(self.poi,self.poiLabels):
            print poiLabel+':   ('+str(self.w.var(poi).getAsymErrorLo())+','+str(self.w.var(poi).getAsymErrorHi())+')'
	
	for poi,poiLabel in zip(self.poi,self.poiLabels):
            print poiLabel+':   ('+str(-self.w.var(poi).getAsymErrorLo()+self.w.var(poi).getAsymErrorHi()/2.)+')'

        #cprime = ROOT.TCanvas('canvas2','')
        #cprime.cd()
        #histo.GetXaxis().SetTitle("#Gamma_{T}")
        #histo.GetYaxis().SetTitle("N toys")
        #histo.Draw()
        #obj.append(histo)
        #print 'Relative error on the total width ',histo.GetRMS()/histo.GetMean()
        print 'Please check the histogram to see that the dist is Gaussian. If not the fit is biased'
        print 'The fit can be biased when floating the width sometimes.'
        

        return c

        
        


