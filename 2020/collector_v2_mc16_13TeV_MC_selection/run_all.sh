source run_mc16_13TeV_Zrad_gammajet_collector.sh
source run_mc16_13TeV_Zrad_dijet_collector.sh
python3 merge.py --signalFiles=gammajetMC/ --backgroundFiles=dijetMC/ --outputFiles=mc16_13TeV.sgn.medium.gammajet.bkg.vetoloose.dijet