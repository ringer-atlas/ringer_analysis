

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
  m_treePath    = '*/HLT/Physval/Egamma/fakes'
else:
  print('Settings pidname and treePath for signal.')
  #pidname    = 'el_lhmedium'
  #pidname    = 'el_lhvloose'
  pidname    = 'el_lhloose'
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

triggerList = []
for ithr in [0, 3, 5, 7, 9 , 12]:
      for iop in ['lhtight', 'lhmedium', 'lhloose', 'lhvloose']:
            no_ringer_chain = Group(Chain("EMU_e%i_%s_nod0_noringer" %(ithr, iop),
                                          "L1_EM3", 
                                          "HLT_e%i_%s_nod0_noringer" %(ithr, iop)),
                                          None if args.fakes else 'el_%s' %(iop), ithr )
            triggerList.append(no_ringer_chain)

            ringer_chain   = Group(Chain("EMU_e%i_%s_nod0_ringer_v1" %(ithr, iop),
                                         "L1_EM3", 
                                         "HLT_e%i_%s_nod0_ringer_v1" %(ithr, iop)),
                                         None if args.fakes else 'el_%s' %(iop), ithr )
            triggerList.append(ringer_chain)


from EfficiencyTools import EfficiencyTool
alg = EfficiencyTool( "Efficiency", dojpsiee=True )

for group in triggerList:
  alg.addGroup( group )

ToolSvc += alg

acc.run(args.nov)
