


import argparse
from prometheus import EventATLAS
from prometheus.enumerations import Dataframe as DataframeEnum
from Gaugi.messenger import LoggingLevel, Logger
from Gaugi import ToolSvc, ToolMgr



mainLogger = Logger.getModuleLogger("job")
parser = argparse.ArgumentParser(description = '', add_help = False)
parser = argparse.ArgumentParser()

parser.add_argument('-i','--inputFile', action='store', 
    dest='inputFile', required = True,
    help = "The input files that will be used to generate the plots")



import sys,os
if len(sys.argv)==1:
  parser.print_help()
  sys.exit(1)

args = parser.parse_args()


from QuadrantTools import QuadrantTool
q_alg = QuadrantTool("Quadrant")
from Gaugi  import restoreStoreGate
sg =  restoreStoreGate( args.inputFile )
q_alg.setStoreGateSvc(sg)


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


outputs = [
            'quadrant_data18_egam2_e5_lhtight_ringer_and_noringer',
            'quadrant_data18_egam2_e5_lhmedium_ringer_and_noringer',
            'quadrant_data18_egam2_e5_lhloose_ringer_and_noringer',
            'quadrant_data18_egam2_e5_lhvloose_ringer_and_noringer'
            ]

legends = ['Both Approved', 'Ringer Rejected', 'Ringer Approved', 'Both Rejected']

names   = [
            'Quadrant Analysis e5 lhtight ringer vs noringer (data18-EGAM2)',
            'Quadrant Analysis e5 lhmedium ringer vs noringer (data18-EGAM2)',
            'Quadrant Analysis e5 lhloose ringer vs noringer (data18-EGAM2)',
            'Quadrant Analysis e5 lhvloose ringer vs noringer (data18-EGAM2)'
            ]

q_alg.plot(outputs, outputs, names,legends=legends, doPDF=True)