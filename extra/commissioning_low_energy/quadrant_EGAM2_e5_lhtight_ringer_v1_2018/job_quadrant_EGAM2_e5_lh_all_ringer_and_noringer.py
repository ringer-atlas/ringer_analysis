
import argparse
from prometheus import EventATLAS
from prometheus.enumerations import Dataframe as DataframeEnum
from Gaugi.messenger import LoggingLevel, Logger
from Gaugi import ToolSvc, ToolMgr


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

parser.add_argument('--Jpsiee', action='store_true', 
    dest='doJpsiee', required = False, 
    help = "Do Jpsiee collection.")

parser.add_argument('--egam7', action='store_true', 
    dest='doEgam7', required = False, 
    help = "The colelcted sample came from EGAM7 skemma.")


import sys,os
if len(sys.argv)==1:
  parser.print_help()
  sys.exit(1)

args = parser.parse_args()

acc = EventATLAS( "EventATLASLoop",
                  inputFiles = args.inputFiles, 
                  treePath= '*/HLT/Egamma/Egamma/probes',
                  dataframe = DataframeEnum.Electron_v1, 
                  outputFile = args.outputFile,
                  level = LoggingLevel.INFO
                  )

from EventSelectionTool import EventSelection, SelectionType, EtCutType
evt = EventSelection('EventSelection')
evt.setCutValue( SelectionType.SelectionOnlineWithRings )

# Do not change this!
if args.doEgam7:
  #pidname = '!VeryLooseLLH_DataDriven_Rel21_Run2_2018'
  pidname = '!el_lhvloose'
else:
  #pidname = 'MediumLLH_DataDriven_Rel21_Run2_2018'
  #pidname = 'el_lhtight'
  #pidname = 'el_lhmedium'
  pidname  = 'el_lhvloose'

#evt.setCutValue( SelectionType.SelectionPID, pidname ) 
evt.setCutValue( EtCutType.L2CaloAbove, 3.)
evt.setCutValue( EtCutType.L2CaloBelow, 15.)
evt.setCutValue( EtCutType.OfflineAbove, 2.)




ToolSvc += evt




from TrigEgammaEmulationTool import Chain

triggerList = [
                # tight
                Chain( "EMU_e5_lhtight_nod0_noringer"  , "L1_EM3", "HLT_e5_lhtight_nod0_noringer"  ),
                Chain( "EMU_e5_lhtight_nod0_ringer_v1" , "L1_EM3", "HLT_e5_lhtight_nod0_ringer_v1" ),
                # medium
                Chain( "EMU_e5_lhmedium_nod0_noringer"  , "L1_EM3", "HLT_e5_lhmedium_nod0_noringer"  ),
                Chain( "EMU_e5_lhmedium_nod0_ringer_v1" , "L1_EM3", "HLT_e5_lhmedium_nod0_ringer_v1" ),
                # loose
                Chain( "EMU_e5_lhloose_nod0_noringer"  , "L1_EM3", "HLT_e5_lhloose_nod0_noringer"  ),
                Chain( "EMU_e5_lhloose_nod0_ringer_v1" , "L1_EM3", "HLT_e5_lhloose_nod0_ringer_v1" ),
                # veryloose
                Chain( "EMU_e5_lhvloose_nod0_noringer"  , "L1_EM3", "HLT_e5_lhvloose_nod0_noringer"  ),
                Chain( "EMU_e5_lhvloose_nod0_ringer_v1" , "L1_EM3", "HLT_e5_lhvloose_nod0_ringer_v1" ),
              ]

# Add all chains into the emulator
emulator = ToolSvc.retrieve( "Emulator" )
for chain in triggerList:
  print(chain.name())
  if not emulator.isValid( chain.name() ):
    emulator+=chain



from QuadrantTools import QuadrantTool
q_alg = QuadrantTool("Quadrant")

q_alg.add_quadrant( 
                # tight
                'HLT_e5_lhtight_nod0_noringer'  , "EMU_e5_lhtight_nod0_noringer", # T2Calo
                'HLT_e5_lhtight_nod0_ringer_v1' , "EMU_e5_lhtight_nod0_ringer_v1" # Ringer v1
                )
q_alg.add_quadrant( 
                # medium
                'HLT_e5_lhmedium_nod0_noringer'  , "EMU_e5_lhmedium_nod0_noringer", # T2Calo
                'HLT_e5_lhmedium_nod0_ringer_v1' , "EMU_e5_lhmedium_nod0_ringer_v1" # Ringer v1
                )
q_alg.add_quadrant(  
                # loose
                'HLT_e5_lhloose_nod0_noringer'  , "EMU_e5_lhloose_nod0_noringer", # T2Calo
                'HLT_e5_lhloose_nod0_ringer_v1' , "EMU_e5_lhloose_nod0_ringer_v1" # Ringer v1
                )
q_alg.add_quadrant( 
                # veryloose
                'HLT_e5_lhvloose_nod0_noringer'  , "EMU_e5_lhvloose_nod0_noringer", # T2Calo
                'HLT_e5_lhvloose_nod0_ringer_v1' , "EMU_e5_lhvloose_nod0_ringer_v1" # Ringer v1
                ) 


etlist = [3.0, 7.0, 10.0, 15.0]
etalist= [ 0.0, 0.6, 0.8, 1.15, 1.37, 1.52, 1.81, 2.01, 2.37, 2.47 ]
#etalist= [ 0.0, 0.8, 1.37, 1.54, 2.37, 2.47]
q_alg.setEtBinningValues(etlist)
q_alg.setEtaBinningValues(etalist)
ToolSvc += q_alg

acc.run(args.nov)