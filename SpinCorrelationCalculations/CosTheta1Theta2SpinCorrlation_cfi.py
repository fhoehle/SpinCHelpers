import ROOT, math

def CosTheta1Theta2(p4_lepSr,p4_bhadSr,p4_toplepSr,p4_tophadSr):
 p4_lep=ROOT.TLorentzVector(p4_lepSr.Px(),p4_lepSr.Py(),p4_lepSr.Pz(),p4_lepSr.E())
 p4_bhad=ROOT.TLorentzVector(p4_bhadSr.Px(),p4_bhadSr.Py(),p4_bhadSr.Pz(),p4_bhadSr.E())
 p4_toplep=ROOT.TLorentzVector(p4_toplepSr.Px(),p4_toplepSr.Py(),p4_toplepSr.Pz(),p4_toplepSr.E())
 p4_tophad=ROOT.TLorentzVector(p4_tophadSr.Px(),p4_tophadSr.Py(),p4_tophadSr.Pz(),p4_tophadSr.E())
 p4_lepBoost=p4_lep
 p4_lepBoost.Boost(ROOT.TVector3(-1.0*p4_toplep.BoostVector().Px(),-1.0*p4_toplep.BoostVector().Py(),-1.0*p4_toplep.BoostVector().Pz()))
 p4_bhadBoost=p4_bhad
 p4_bhadBoost.Boost(ROOT.TVector3(-1.0*p4_tophad.BoostVector().Px(),-1.0*p4_tophad.BoostVector().Py(),-1.0*p4_tophad.BoostVector().Pz()))
 p4_toplepBoost=p4_toplep
 p4_toplepBoost.Boost(ROOT.TVector3(-1.0*(p4_toplep+p4_tophad).BoostVector().Px(),-1.0*(p4_toplep+p4_tophad).BoostVector().Py(),-1.0*(p4_toplep+p4_tophad).BoostVector().Pz()))
 p4_tophadBoost=p4_tophad
 p4_tophadBoost.Boost(ROOT.TVector3(-1.0*(p4_toplep+p4_tophad).BoostVector().Px(),-1.0*(p4_toplep+p4_tophad).BoostVector().Py(),-1.0*(p4_toplep+p4_tophad).BoostVector().Pz()))
 return [math.cos(p4_lepBoost.Vect().Angle(p4_toplepBoost.Vect())),math.cos(p4_bhadBoost.Vect().Angle(p4_tophadBoost.Vect()))]

