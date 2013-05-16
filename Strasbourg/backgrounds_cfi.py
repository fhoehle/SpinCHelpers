import ROOT
#
## internal function to determine site 
def inputPath()
  import os
  if '/opt__sbg__data__safe1' in os.getcwd():
    return '/opt/sbg/data/safe1/cms/fhoehle/MyIPHC_Unfolding/UnfoldingIPHC/inputs/'
##
def deltaPhiBackgroundHistScaled():
  bgFile = ROOT.TFile(inputPath()+"/selected_Data_BG.root");
  backHistNames = [["DeltaPhiLLept_mumu_afterbtag1_TTbarBkg","DeltaPhiLLept_mumu_afterbtag1_DYToLL_M10-50","DeltaPhiLLept_mumu_afterbtag1_Zjets",
  	"DeltaPhiLLept_mumu_afterbtag1_Wjets","DeltaPhiLLept_mumu_afterbtag1_TtW","DeltaPhiLLept_mumu_afterbtag1_TbartW","DeltaPhiLLept_mumu_afterbtag1_WZ",
  	"DeltaPhiLLept_mumu_afterbtag1_ZZ","DeltaPhiLLept_mumu_afterbtag1_WW"],
  	["DeltaPhiLLept_emu_afterbtag1_TTbarBkg","DeltaPhiLLept_emu_afterbtag1_DYToLL_M10-50","DeltaPhiLLept_emu_afterbtag1_Zjets",
  	"DeltaPhiLLept_emu_afterbtag1_Wjets","DeltaPhiLLept_emu_afterbtag1_TtW","DeltaPhiLLept_emu_afterbtag1_TbartW","DeltaPhiLLept_emu_afterbtag1_WZ",
  	"DeltaPhiLLept_emu_afterbtag1_ZZ","DeltaPhiLLept_emu_afterbtag1_WW"],
  	["DeltaPhiLLept_ee_afterbtag1_TTbarBkg","DeltaPhiLLept_ee_afterbtag1_DYToLL_M10-50","DeltaPhiLLept_ee_afterbtag1_Zjets",
  	"DeltaPhiLLept_ee_afterbtag1_Wjets","DeltaPhiLLept_ee_afterbtag1_TtW","DeltaPhiLLept_ee_afterbtag1_TbartW","DeltaPhiLLept_ee_afterbtag1_WZ",
  	"DeltaPhiLLept_ee_afterbtag1_ZZ","DeltaPhiLLept_ee_afterbtag1_WW"]]
  
  bckgHist_mumu = bgFile.Get(backHistNames[0][0]).Clone("deltaPhiBkg_mumu");bckgHist_mumu.Reset("ICE")
  bckgHist_emu = bgFile.Get(backHistNames[1][0]).Clone("deltaPhiBkg_emu");bckgHist_emu.Reset("ICE")
  bckgHist_ee = bgFile.Get(backHistNames[2][0]).Clone("deltaPhiBkg_ee");bckgHist_ee.Reset("ICE")
  ## mumu
  for bkg in backHistNames[0]:
    bckgHist_mumu.Add(bgFile.Get(bkg))
  ## emu
  for bkg in backHistNames[1]:
    bckgHist_emu.Add(bgFile.Get(bkg))
  ## ee
  for bkg in backHistNames[2]:
    bckgHist_ee.Add(bgFile.Get(bkg))
  print "mumu bkg ",bckgHist_mumu.Integral(); print "emu bkg ",bckgHist_emu.Integral(); print "ee bkg ",bckgHist_ee.Integral()
  bckgHist = bckgHist_mumu.Clone("deltaPhiBkg"); bckgHist.Reset("ICE")
  bckgHist.Add(bckgHist_mumu);bckgHist.Add(bckgHist_emu);bckgHist.Add(bckgHist_ee)
  return bckgHist
def deltaPhiSignalHistScaled():
  signalFile = ROOT.TFile(inputPath()+'/selected_Data_BG.root')
  signalHistmumu = signalFile.Get("DeltaPhiLLept_mumu_afterbtag1_TTbarSig").Clone("DeltaPhiLLept_mumu_afterbtag1_TTbarSig");
  signalHistmumu.Sumw2();signalHistmumu.Scale(1.0/signalHistmumu.Integral())
  signalHistemu = signalFile.Get("DeltaPhiLLept_ee_afterbtag1_TTbarSig").Clone("DeltaPhiLLept_ee_afterbtag1_TTbarSig");
  signalHistemu.Sumw2();signalHistemu.Scale(1.0/signalHistemu.Integral())
  signalHistee = signalFile.Get("DeltaPhiLLept_emu_afterbtag1_TTbarSig").Clone("DeltaPhiLLept_emu_afterbtag1_TTbarSig");
  signalHistee.Sumw2();signalHistee.Scale(1.0/signalHistee.Integral())
  signalDeltaPhi = signalHistmumu.Clone("signalDeltaPhi");signalDeltaPhi.Reset("ICE");
  signalDeltaPhi.Add(signalHistmumu,1880.16);
  signalDeltaPhi.Add(signalHistemu,5654.72);
  signalDeltaPhi.Add(signalHistee,1503.76);
  return signalDeltaPhi
