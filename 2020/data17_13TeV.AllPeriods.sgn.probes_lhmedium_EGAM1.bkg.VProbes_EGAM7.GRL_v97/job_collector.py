




from prometheus import EventATLAS
from prometheus.enumerations import Dataframe as DataframeEnum
from Gaugi.messenger import LoggingLevel, Logger
from Gaugi import ToolSvc, ToolMgr
import argparse
mainLogger = Logger.getModuleLogger("job")
parser = argparse.ArgumentParser(description = '', add_help = False)
parser = argparse.ArgumentParser()


parser.add_argument('-i','--inputFiles', action='store',
    dest='inputFiles', required = True, nargs='+',
    help = "The input files that will be used to generate the plots")

parser.add_argument('-o','--outputFile', action='store',
    dest='outputFile', required = False, default = None,
    help = "The output store name.")

parser.add_argument('-n','--nov', action='store',
    dest='nov', required = False, default = -1, type=int,
    help = "Number of events.")

parser.add_argument('--jpsi', action='store_true',
    dest='doJpsi', required = False,
    help = "Do Jpsi collection.")

parser.add_argument('--egam7', action='store_true',
    dest='doEgam7', required = False,
    help = "The colelcted sample came from EGAM7 skemma.")

parser.add_argument('--oldGrid', action='store_true',
    dest='doOldGrid', required = False,
    help = "Use the old grid implemented during 2017 to ringer v6 (20 phase spaces). default is 25 bins")

parser.add_argument('--jf17', action='store_true', 
    dest='jf17', required = False, 
    help = "The collected samples came from JF17 (veto mc)")


parser.add_argument('--oldPath', action='store_true', 
    dest='doOldPath', required = False, 
    help = "Should be include descripton here")




import sys,os
if len(sys.argv)==1:
  parser.print_help()
  sys.exit(1)

args = parser.parse_args()


isFake = True if (args.jf17 or args.doEgam7) else False


if args.doOldPath:
  treePath= '*/HLT/Physval/Egamma/fakes' if isFake else '*/HLT/Physval/Egamma/probes'
else:
  treePath= '*/HLT/Egamma/Egamma/fakes' if isFake else '*/HLT/Egamma/Egamma/probes'



acc = EventATLAS(  "EventATLASLoop",
                  inputFiles = args.inputFiles,
                  treePath = treePath,
                  dataframe = DataframeEnum.Electron_v1,
                  outputFile = args.outputFile,
                  level = LoggingLevel.INFO,
                )



from EventSelectionTool import EventSelection, SelectionType, EtCutType

evt = EventSelection('EventSelection')

evt.setCutValue( SelectionType.SelectionOnlineWithRings )


# Do not change this!
if args.doEgam7:
  pidname = '!el_lhvloose'
elif args.jf17:
  pidname = '!mc_isTruthElectronAny'
else:
  pidname = 'el_lhmedium'
  #pidname = 'el_lhtight'

print( pidname )


if args.doJpsi:
    evt.setCutValue( SelectionType.SelectionPID, pidname )
    evt.setCutValue( EtCutType.L2CaloAbove, 4 )
    evt.setCutValue( EtCutType.L2CaloBelow, 15 )
    evt.setCutValue( EtCutType.OfflineAbove, 2 )
else:
    evt.setCutValue( SelectionType.SelectionPID, pidname )
    evt.setCutValue( EtCutType.L2CaloAbove , 15)

ToolSvc += evt



from TrigEgammaEmulationTool import installTrigEgammaL2CaloSelectors, installElectronL2CaloRingerSelector_v6, installElectronL2CaloRingerSelector_v8
installTrigEgammaL2CaloSelectors()
#installElectronL2CaloRingerSelector_v6()
#installElectronL2CaloRingerSelector_v8()



from CollectorTool import Collector
alg = Collector( 'Collector' , 
                  OutputFile = args.outputFile.replace('.root',''), 
                  )




if args.doOldGrid:
  etabins = [0.0, 0.8, 1.37, 1.54, 2.50]
else:
  etabins = [0.0, 0.8, 1.37, 1.54, 2.37, 2.50]


if args.doJpsi:
    etbins = [0.0, 7.0, 10.0, 15.0]
else:
    etbins  = [15.0, 20.0, 30.0, 40.0, 50.0, 1000000.0]

alg.setEtBinningValues( etbins   )
alg.setEtaBinningValues( etabins )


alg.AddFeature( "T0HLTElectronT2CaloTight"        )
alg.AddFeature( "T0HLTElectronT2CaloMedium"       )
alg.AddFeature( "T0HLTElectronT2CaloLoose"        )
alg.AddFeature( "T0HLTElectronT2CaloVLoose"       )


#alg.AddFeature( "T0HLTElectronRingerTight_v6"       )
#alg.AddFeature( "T0HLTElectronRingerMedium_v6"      )
#alg.AddFeature( "T0HLTElectronRingerLoose_v6"       )
#alg.AddFeature( "T0HLTElectronRingerVeryLoose_v6"   )
#
#
#alg.AddFeature( "T0HLTElectronRingerTight_v8"       )
#alg.AddFeature( "T0HLTElectronRingerMedium_v8"      )
#alg.AddFeature( "T0HLTElectronRingerLoose_v8"       )
#alg.AddFeature( "T0HLTElectronRingerVeryLoose_v8"   )


ToolSvc += alg

acc.run(args.nov)







