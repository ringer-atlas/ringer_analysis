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

parser.add_argument('--Zrad', action='store_true',
    dest='doZrad', required = False,
    help = "Do Zrad collection.")

parser.add_argument('--fakes', action='store_true',
    dest='doFakes', required = False,
    help = "The colelcted sample came from EGAM7 skemma.")

import sys,os
if len(sys.argv)==1:
  parser.print_help()
  sys.exit(1)

args = parser.parse_args()

acc = EventATLAS(  "EventATLASLoop",
                  inputFiles = args.inputFiles,
                  treePath= '*/HLT/PhysVal/Egamma/fakes' if args.doFakes else '*/HLT/PhysVal/Egamma/photons',
                  dataframe = DataframeEnum.Photon_v1,
                  outputFile = args.outputFile,
                  # outputFile = 'dummy.root',
                  level = LoggingLevel.INFO,
                )

from EventSelectionTool import EventSelection, SelectionType, EtCutType

evt = EventSelection('EventSelection')
evt.setCutValue( EtCutType.L2CaloAbove , 15)
if args.doZrad:
    pidname = 'ph_medium'
elif args.doFakes:
    pidname = '!ph_loose'
else:
    pidname = 'ph_medium'

ToolSvc += evt

evt.setCutValue (SelectionType.SelectionPID, pidname)

from TrigEgammaEmulationTool import installTrigEgammaL2PhotonCaloSelectors
installTrigEgammaL2PhotonCaloSelectors()


from CollectorTool import Collector
alg = Collector( 'Collector' , OutputFile = args.outputFile.replace('.root',''), 
                )

etabins = [0.0, 0.8, 1.37, 1.54, 2.37, 2.50]
etbins  = [15.0, 20.0, 30.0, 40.0, 50.0, 1000000.0]
alg.setEtBinningValues( etbins   )
alg.setEtaBinningValues( etabins )
alg.doTrigger  = True

alg.AddFeature( "T0HLTPhotonT2CaloTight"        )
alg.AddFeature( "T0HLTPhotonT2CaloMedium"       )
alg.AddFeature( "T0HLTPhotonT2CaloLoose"        )

ToolSvc += alg

acc.run(args.nov)
