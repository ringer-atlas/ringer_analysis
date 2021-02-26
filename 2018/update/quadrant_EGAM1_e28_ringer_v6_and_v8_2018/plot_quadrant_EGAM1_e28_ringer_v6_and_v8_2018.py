


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
alg = QuadrantTool("Quadrant",  dataframe = DataframeEnum.Electron_v1)
from Gaugi  import restoreStoreGate
sg =  restoreStoreGate( args.inputFile )
alg.setStoreGateSvc(sg)

alg.add_quadrant( 'HLT_e28_lhtight_nod0_ringer_v6_ivarloose' , "EMU_e28_lhtight_nod0_ringer_v6_ivarloose", # Ringer v6
                  'HLT_e28_lhtight_nod0_ringer_v8_ivarloose' , "EMU_e28_lhtight_nod0_ringer_v8_ivarloose") # Ringer v8



etlist = [15.0,20.0,25.0,30.0,35.0,40.0,45.0,50.0,50000.0] 
etalist= [ 0.0, 0.6, 0.8, 1.15, 1.37, 1.52, 1.81, 2.01, 2.37, 2.47 ]
alg.setEtBinningValues(etlist)
alg.setEtaBinningValues(etalist)

ToolSvc += alg

outputs = [
            'plot_quadrant_EGAM1_e28_ringer_v6_and_v8_2018',
            ]

legends = ['Both Approved', 'Ringer v8 Rejected', 'Ringer v8 Approved', 'Both Rejected']

alg.plot(outputs, outputs, ['Quadrant Analysis e28 lhtight ringer v6/v8 (data18)'] ,legends=legends, doPDF=True)






