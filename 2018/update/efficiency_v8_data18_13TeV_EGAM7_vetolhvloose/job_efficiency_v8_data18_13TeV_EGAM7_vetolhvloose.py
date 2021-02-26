

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

import sys,os
if len(sys.argv)==1:
  parser.print_help()
  sys.exit(1)

args = parser.parse_args()



acc = EventATLAS( "EventATLASLoop",
                  inputFiles = args.inputFiles, 
                  #treePath= '*/HLT/Physval/Egamma/fakes' ,#if args.doEgam7 else '*/HLT/Physval/Egamma/probes',
                  treePath= '*/HLT/Egamma/Egamma/fakes' ,
                  dataframe = DataframeEnum.Electron_v1, 
                  outputFile = args.outputFile,
                  level = LoggingLevel.INFO
                  )



from EventSelectionTool import EventSelection, SelectionType, EtCutType

evt = EventSelection('EventSelection', dataframe = DataframeEnum.Electron_v1)
evt.setCutValue( SelectionType.SelectionOnlineWithRings )

pidname = '!el_lhvloose'

evt.setCutValue( SelectionType.SelectionPID, pidname ) 
evt.setCutValue( EtCutType.L2CaloAbove , 15)
ToolSvc += evt


from TrigEgammaEmulationTool import Chain, Group, TDT

triggerList = [
                # e17 lhvloose
                Group( TDT( "TDT_e17_lhvloose_nod0_L1EM15VHI" , "HLT_e17_lhvloose_nod0_L1EM15VHI"   ), None, 17 ),
                Group( Chain( "EMU_e17_lhvloose_nod0_noringer_L1EM15VHI"      , "L1_EM15VHI", "HLT_e17_lhvloose_nod0_noringer_L1EM15VHI"    ), None, 17 ),
                Group( Chain( "EMU_e17_lhvloose_nod0_ringer_v6_L1EM15VHI"     , "L1_EM15VHI", "HLT_e17_lhvloose_nod0_ringer_v6_L1EM15VHI"   ), None, 17 ),
                Group( Chain( "EMU_e17_lhvloose_nod0_ringer_v8_L1EM15VHI"     , "L1_EM15VHI", "HLT_e17_lhvloose_nod0_ringer_v8_L1EM15VHI"   ), None, 17 ),
                Group( Chain( "EMU_e17_lhvloose_nod0_ringer_v10_L1EM15VHI"    , "L1_EM15VHI", "HLT_e17_lhvloose_nod0_ringer_v10_L1EM15VHI"  ), None, 17 ),


                # e17 lhloose
                Group( TDT( "TDT_e17_lhloose_nod0" , "HLT_e17_lhloose_nod0"   ), None, 17 ),
                Group( Chain( "EMU_e17_lhloose_nod0_noringer"                  , "L1_EM15VH", "HLT_e17_lhloose_nod0_noringer"    ), None, 17 ),
                Group( Chain( "EMU_e17_lhloose_nod0_ringer_v6"                 , "L1_EM15VH", "HLT_e17_lhloose_nod0_ringer_v6"   ), None, 17 ),
                Group( Chain( "EMU_e17_lhloose_nod0_ringer_v8"                 , "L1_EM15VH", "HLT_e17_lhloose_nod0_ringer_v8"   ), None, 17 ),
                Group( Chain( "EMU_e17_lhloose_nod0_ringer_v10"                , "L1_EM15VH", "HLT_e17_lhloose_nod0_ringer_v10"  ), None, 17 ),


                 # e60 lhmedium
                Group( TDT( "TDT_e60_lhmedium_nod0" , "HLT_e60_lhmedium_nod0"   ), None, 60 ),
                Group( Chain( "EMU_e60_lhmedium_nod0_noringer'"               , "L1_EM22VHI", "HLT_e60_lhmedium_nod0_noringer"   ), None, 60 ),
                Group( Chain( "EMU_e60_lhmedium_nod0_ringer_v6"               , "L1_EM22VHI", "HLT_e60_lhmedium_nod0_ringer_v6"  ), None, 60 ),
                Group( Chain( "EMU_e60_lhmedium_nod0_ringer_v8"               , "L1_EM22VHI", "HLT_e60_lhmedium_nod0_ringer_v8"  ), None, 60 ),
                Group( Chain( "EMU_e60_lhmedium_nod0_ringer_v10"              , "L1_EM22VHI", "HLT_e60_lhmedium_nod0_ringer_v10" ), None, 60 ),


                # e28 lhtight
                Group( TDT( "TDT_e28_lhtight_nod0_noringer_ivarloose" , "HLT_e28_lhtight_nod0_noringer_ivarloose"   ),None, 28 ),
                Group( Chain( "EMU_e28_lhtight_nod0_noringer_ivarloose"       , "L1_EM24VHI", "HLT_e28_lhtight_nod0_noringer_ivarloose"   ), None, 28 ),
                Group( Chain( "EMU_e28_lhtight_nod0_ringer_v6_ivarloose"      , "L1_EM24VHI", "HLT_e28_lhtight_nod0_ringer_v6_ivarloose"  ), None, 28 ),
                Group( Chain( "EMU_e28_lhtight_nod0_ringer_v8_ivarloose"      , "L1_EM24VHI", "HLT_e28_lhtight_nod0_ringer_v8_ivarloose"  ), None, 28 ),
                Group( Chain( "EMU_e28_lhtight_nod0_ringer_v10_ivarloose"     , "L1_EM24VHI", "HLT_e28_lhtight_nod0_ringer_v10_ivarloose" ), None, 28 ),
              ]



from EfficiencyTools import EfficiencyTool
alg = EfficiencyTool( "Efficiency", dataframe = DataframeEnum.Electron_v1)


for group in triggerList:
  alg.addGroup( group )

ToolSvc += alg

acc.run(args.nov)





