

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

parser.add_argument('--fake', action='store_true', 
    dest='fakes', required = False, 
    help = "Set the pidname and treePath for background.")

import sys,os
if len(sys.argv)==1:
  parser.print_help()
  sys.exit(1)

args = parser.parse_args()


if args.fakes:
  print('Setting pidname and treePath for background...')
  pidname       = '!el_lhvloose'
  m_treePath    = '*/HLT/Egamma/Egamma/fakes'
else:
  print('Settings pidname and treePath for signal.')
  #pidname    = 'el_lhmedium'
  pidname    = 'el_lhvloose'
  m_treePath = '*/HLT/Egamma/Egamma/probes'

acc = EventATLAS( "EventATLASLoop",
                  inputFiles = args.inputFiles, 
                  treePath= m_treePath,
                  dataframe = DataframeEnum.Electron_v1, 
                  outputFile = args.outputFile,
                  level = LoggingLevel.INFO
                  )


# EventSelection Configuration
from EventSelectionTool import EventSelection, SelectionType, EtCutType
evt = EventSelection('EventSelection')
evt.setCutValue( SelectionType.SelectionOnlineWithRings )
evt.setCutValue( SelectionType.SelectionPID, pidname ) 
evt.setCutValue( EtCutType.L2CaloAbove , 3)
evt.setCutValue( EtCutType.L2CaloBelow , 15)

ToolSvc += evt


from TrigEgammaEmulationTool import Chain, Group, TDT
# Trigger list 
if args.fakes:
      print('Measuring Fake...')

      triggerList = [
                # HLT_e5_lhvloose_nod0
                #Group(Chain("EMU_e5_lhvloose_nod0_noringer", "L1_EM3", "HLT_e5_lhvloose_nod0_noringer"),
                #      None, 5 ),
                #Group(Chain("EMU_e5_lhvloose_nod0_ringer_v1", "L1_EM3", "HLT_e5_lhvloose_nod0_ringer_v1"), 
                #      None, 5 ),
                # HLT_e5_lhloose_nod0
                #Group(Chain("EMU_e5_lhloose_nod0_noringer", "L1_EM3", "HLT_e5_lhloose_nod0_noringer"),
                #      None, 5 ),
                #Group(Chain("EMU_e5_lhloose_nod0_ringer_v1", "L1_EM3", "HLT_e5_lhloose_nod0_ringer_v1"), 
                #      None, 5 ),
                # HLT_e5_lhmedium_nod0
                #Group(Chain("EMU_e5_lhmedium_nod0_noringer", "L1_EM3", "HLT_e5_lhmedium_nod0_noringer"),
                #      None, 5 ),
                #Group(Chain("EMU_e5_lhmedium_nod0_ringer_v1", "L1_EM3", "HLT_e5_lhmedium_nod0_ringer_v1"), 
                #      None, 5 ),
                # HLT_e5_lhtight_nod0
                #Group(Chain("EMU_e5_lhtight_nod0_noringer", "L1_EM3", "HLT_e5_lhtight_nod0_noringer"),
                #      None, 5 ),
                #Group(Chain("EMU_e5_lhtight_nod0_ringer_v1", "L1_EM3", "HLT_e5_lhtight_nod0_ringer_v1"), 
                #      None, 5 ),
                # HLT_e7_lhmedium_nod0
                Group(Chain("EMU_e7_lhmedium_nod0_noringer", "L1_EM3", "HLT_e7_lhmedium_nod0_noringer"), 
                      None, 7),
                Group(Chain("EMU_e7_lhmedium_nod0_ringer_v1", "L1_EM3", "HLT_e7_lhmedium_nod0_ringer_v1"), 
                      None, 7),
                # HLT_e9_lhloose_nod0
                #Group(Chain("EMU_e9_lhloose_nod0_noringer", "L1_EM3", "HLT_e9_lhloose_nod0_noringer"), 
                #      None, 9),
                #Group(Chain("EMU_e9_lhloose_nod0_ringer_v1", "L1_EM3", "HLT_e9_lhloose_nod0_ringer_v1"), 
                #      None, 9),
                # HLT_e9_lhmedium_nod0
                Group(Chain("EMU_e9_lhmedium_nod0_noringer", "L1_EM3", "HLT_e9_medium_nod0_noringer"), 
                      None, 9),
                Group(Chain("EMU_e9_lhmedium_nod0_ringer_v1", "L1_EM3", "HLT_e9_medium_nod0_ringer_v1"), 
                      None, 9),
                # HLT_e9_lhtight_nod0
                #Group(Chain("EMU_e9_lhtight_nod0_noringer", "L1_EM3", "HLT_e9_lhtight_nod0_noringer"), 
                #      None, 9),
                #Group(Chain("EMU_e9_lhtight_nod0_ringer_v1", "L1_EM3", "HLT_e9_lhtight_nod0_ringer_v1"), 
                #      None, 9),
                # HLT_e12_lhmedium_nod0
                Group(Chain("EMU_e12_lhmedium_nod0_noringer", "L1_EM3", "HLT_e12_lhmedium_nod0_noringer"), 
                      None, 12),
                Group(Chain("EMU_e12_lhmedium_nod0_ringer_v1", "L1_EM3", "HLT_e12_lhmedium_nod0_ringer_v1"), 
                      None, 12),
      ]

else:
      print('Measuring Signal... ')
      triggerList = [
                # HLT_e5_lhvloose_nod0
                Group(Chain("EMU_e5_lhvloose_nod0_noringer", "L1_EM3", "HLT_e5_lhvloose_nod0_noringer"),
                      'el_lhvloose', 5 ),
                Group(Chain("EMU_e5_lhvloose_nod0_ringer_v1", "L1_EM3", "HLT_e5_lhvloose_nod0_ringer_v1"), 
                      'el_lhvloose', 5 ),
                # HLT_e5_lhtight_nod0
                Group(Chain("EMU_e5_lhtight_nod0_noringer", "L1_EM3", "HLT_e5_lhtight_nod0_noringer"),
                      'el_lhtight', 5 ),
                Group(Chain("EMU_e5_lhtight_nod0_ringer_v1", "L1_EM3", "HLT_e5_lhtight_nod0_ringer_v1"), 
                      'el_lhtight', 5 ),
      ]
'''  
      triggerList = [
                # HLT_e5_lhvloose_nod0
                Group(Chain("EMU_e5_lhvloose_nod0_noringer", "L1_EM3", "HLT_e5_lhvloose_nod0_noringer"),
                      'el_lhvloose', 5 ),
                Group(Chain("EMU_e5_lhvloose_nod0_ringer_v1", "L1_EM3", "HLT_e5_lhvloose_nod0_ringer_v1"), 
                      'el_lhvloose', 5 ),
                # HLT_e5_lhloose_nod0
                Group(Chain("EMU_e5_lhloose_nod0_noringer", "L1_EM3", "HLT_e5_lhloose_nod0_noringer"),
                      'el_lhloose', 5 ),
                Group(Chain("EMU_e5_lhloose_nod0_ringer_v1", "L1_EM3", "HLT_e5_lhloose_nod0_ringer_v1"), 
                      'el_lhloose', 5 ),
                # HLT_e5_lhmedium_nod0
                Group(Chain("EMU_e5_lhmedium_nod0_noringer", "L1_EM3", "HLT_e5_lhmedium_nod0_noringer"),
                      'el_lhmedium', 5 ),
                Group(Chain("EMU_e5_lhmedium_nod0_ringer_v1", "L1_EM3", "HLT_e5_lhmedium_nod0_ringer_v1"), 
                      'el_lhmedium', 5 ),
                # HLT_e5_lhtight_nod0
                Group(Chain("EMU_e5_lhtight_nod0_noringer", "L1_EM3", "HLT_e5_lhtight_nod0_noringer"),
                      'el_lhtight', 5 ),
                Group(Chain("EMU_e5_lhtight_nod0_ringer_v1", "L1_EM3", "HLT_e5_lhtight_nod0_ringer_v1"), 
                      'el_lhtight', 5 ),
                # HLT_e7_lhmedium_nod0
                Group(Chain("EMU_e7_lhmedium_nod0_noringer", "L1_EM3", "HLT_e7_lhmedium_nod0_noringer"), 
                      'el_lhmedium', 7),
                Group(Chain("EMU_e7_lhmedium_nod0_ringer_v1", "L1_EM3", "HLT_e7_lhmedium_nod0_ringer_v1"), 
                      'el_lhmedium', 7),
                # HLT_e9_lhloose_nod0
                Group(Chain("EMU_e9_lhloose_nod0_noringer", "L1_EM3", "HLT_e9_lhloose_nod0_noringer"), 
                      'el_lhloose', 9),
                Group(Chain("EMU_e9_lhloose_nod0_ringer_v1", "L1_EM3", "HLT_e9_lhloose_nod0_ringer_v1"), 
                      'el_lhloose', 9),
                # HLT_e9_lhmedium_nod0
                Group(Chain("EMU_e9_lhmedium_nod0_noringer", "L1_EM3", "HLT_e9_medium_nod0_noringer"), 
                      'el_lhmedium', 9),
                Group(Chain("EMU_e9_lhmedium_nod0_ringer_v1", "L1_EM3", "HLT_e9_medium_nod0_ringer_v1"), 
                      'el_lhmedium', 9),
                # HLT_e9_lhtight_nod0
                Group(Chain("EMU_e9_lhtight_nod0_noringer", "L1_EM3", "HLT_e9_lhtight_nod0_noringer"), 
                      'el_lhtight', 9),
                Group(Chain("EMU_e9_lhtight_nod0_ringer_v1", "L1_EM3", "HLT_e9_lhtight_nod0_ringer_v1"), 
                      'el_lhtight', 9),
                # HLT_e12_lhmedium_nod0
                Group(Chain("EMU_e12_lhmedium_nod0_noringer", "L1_EM3", "HLT_e12_lhmedium_nod0_noringer"), 
                      'el_lhmedium', 12),
                Group(Chain("EMU_e12_lhmedium_nod0_ringer_v1", "L1_EM3", "HLT_e12_lhmedium_nod0_ringer_v1"), 
                      'el_lhmedium', 12),
      ]
'''

      

print(' MICAEL : ', args.outputFile)

from EfficiencyTools import EfficiencyTool
alg = EfficiencyTool( "Efficiency", dojpsiee=True, json_name=args.outputFile )

for group in triggerList:
  alg.addGroup( group )

ToolSvc += alg

acc.run(args.nov)