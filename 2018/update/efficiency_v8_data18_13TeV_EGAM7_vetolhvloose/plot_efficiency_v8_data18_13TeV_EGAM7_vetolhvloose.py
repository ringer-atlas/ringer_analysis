
from ROOT import kBlack,kBlue,kRed,kAzure,kGreen,kMagenta,kCyan,kOrange,kGray,kYellow,kWhite,TColor
from Gaugi.messenger import LoggingLevel, Logger
from Gaugi.storage import  restoreStoreGate
from EfficiencyTools import PlotProfiles


from ROOT import gROOT
gROOT.SetBatch(True)


mainLogger = Logger.getModuleLogger("job")
mainLogger.level = LoggingLevel.INFO

theseColors = [kBlack, kGray+2, kBlue-4, kBlue-2]


def plot_table( sg, logger, trigger, basepath ):
  triggerLevels = ['L1Calo','L2Calo','L2','EFCalo','HLT']
  logger.info( '{:-^78}'.format((' %s ')%(trigger)) ) 
  
  for trigLevel in triggerLevels:
    dirname = basepath+'/'+trigger+'/Efficiency/'+trigLevel
    total  = sg.histogram( dirname+'/eta' ).GetEntries()
    passed = sg.histogram( dirname+'/match_eta' ).GetEntries()
    eff = passed/float(total) * 100. if total>0 else 0
    eff=('%1.2f')%(eff); passed=('%d')%(passed); total=('%d')%(total)
    stroutput = '| {0:<30} | {1:<5} ({2:<5}, {3:<5}) |'.format(trigLevel,eff,passed,total)
    logger.info(stroutput)
  logger.info( '{:-^78}'.format((' %s ')%('-')))





inputFile = '../phd_data/efficiency_v8_data18_13TeV_EGAM7_vetolhvloose/efficiency_v8_data18_13TeV_EGAM7_vetolhvloose.root'
basepath = 'Event/EfficiencyTool'

sg =  restoreStoreGate( inputFile )



triggers = [ 
             "EMU_e17_lhvloose_nod0_noringer_L1EM15VHI",
             "EMU_e17_lhvloose_nod0_ringer_v6_L1EM15VHI",
             "EMU_e17_lhvloose_nod0_ringer_v8_L1EM15VHI",
             ]


eff_et  = [ sg.histogram( basepath+'/'+trigger+'/Efficiency/HLT/eff_et' ) for trigger in triggers ]
eff_eta = [ sg.histogram( basepath+'/'+trigger+'/Efficiency/HLT/eff_eta' ) for trigger in triggers ]
eff_phi = [ sg.histogram( basepath+'/'+trigger+'/Efficiency/HLT/eff_phi' ) for trigger in triggers ]
eff_mu  = [ sg.histogram( basepath+'/'+trigger+'/Efficiency/HLT/eff_mu' ) for trigger in triggers ]
          

legends = ['noringer', 'ringer v6', 'ringer v8']

PlotProfiles( eff_et, legends=legends,runLabel='data18 13TeV', outname='efficiency_v8_data18_13TeV_EGAM1_probes_lhmedium_e17_lhvloose_eff_et.pdf', theseColors=theseColors,
              extraText1='e17_lhvloose_nod0_L1EM15VHI',doRatioCanvas=False, legendX1=.65, xlabel='E_{T}', rlabel='Trigger/Ref.',ylabel='Trigger Efficiency')

PlotProfiles( eff_eta, legends=legends,runLabel='data18 13TeV', outname='efficiency_v8_data18_13TeV_EGAM1_probes_lhmedium_e17_lhvloose_eff_eta.pdf',theseColors=theseColors,
              extraText1='e17_lhvloose_nod0_L1EM15VHI',doRatioCanvas=False, legendX1=.65, xlabel='#eta', rlabel='Trigger/Ref.',ylabel='Trigger Efficiency')

PlotProfiles( eff_phi, legends=legends,runLabel='data18 13TeV', outname='efficiency_v8_data18_13TeV_EGAM1_probes_lhmedium_e17_lhvloose_eff_phi.pdf',theseColors=theseColors,
              extraText1='e17_lhvloose_nod0_L1EM15VHI',doRatioCanvas=False, legendX1=.65, xlabel='#phi', rlabel='Trigger/Ref.',ylabel='Trigger Efficiency')

PlotProfiles( eff_mu, legends=legends,runLabel='data18 13TeV', outname='efficiency_v8_data18_13TeV_EGAM1_probes_lhmedium_e17_lhvloose_eff_mu.pdf',theseColors=theseColors,
              extraText1='e17_lhvloose_nod0_L1EM15VHI',doRatioCanvas=False, legendX1=.65, xlabel='<#mu>', rlabel='Trigger/Ref.',ylabel='Trigger Efficiency')


eff_et  = [ sg.histogram( basepath+'/'+trigger+'/Efficiency/L2Calo/eff_et' ) for trigger in triggers ]
eff_eta = [ sg.histogram( basepath+'/'+trigger+'/Efficiency/L2Calo/eff_eta' ) for trigger in triggers ]
eff_phi = [ sg.histogram( basepath+'/'+trigger+'/Efficiency/L2Calo/eff_phi' ) for trigger in triggers ]
eff_mu  = [ sg.histogram( basepath+'/'+trigger+'/Efficiency/L2Calo/eff_mu' ) for trigger in triggers ]
          
PlotProfiles( eff_et, legends=legends,runLabel='data18 13TeV', outname='efficiency_v8_data18_13TeV_EGAM1_probes_lhmedium_e17_lhvloose_eff_fast_et.pdf', theseColors=theseColors,
              extraText1='e17_lhvloose_nod0_L1EM15VHI',doRatioCanvas=False, legendX1=.65, xlabel='E_{T}', rlabel='Trigger/Ref.',ylabel='Trigger Efficiency')

PlotProfiles( eff_eta, legends=legends,runLabel='data18 13TeV', outname='efficiency_v8_data18_13TeV_EGAM1_probes_lhmedium_e17_lhvloose_eff_fast_eta.pdf',theseColors=theseColors,
              extraText1='e17_lhvloose_nod0_L1EM15VHI',doRatioCanvas=False, legendX1=.65, xlabel='#eta', rlabel='Trigger/Ref.',ylabel='Trigger Efficiency')

PlotProfiles( eff_phi, legends=legends,runLabel='data18 13TeV', outname='efficiency_v8_data18_13TeV_EGAM1_probes_lhmedium_e17_lhvloose_eff_fast_phi.pdf',theseColors=theseColors,
              extraText1='e17_lhvloose_nod0_L1EM15VHI',doRatioCanvas=False, legendX1=.65, xlabel='#phi', rlabel='Trigger/Ref.',ylabel='Trigger Efficiency')

PlotProfiles( eff_mu, legends=legends,runLabel='data18 13TeV', outname='efficiency_v8_data18_13TeV_EGAM1_probes_lhmedium_e17_lhvloose_eff_fast_mu.pdf',theseColors=theseColors,
              extraText1='e17_lhvloose_nod0_L1EM15VHI',doRatioCanvas=False, legendX1=.65, xlabel='<#mu>', rlabel='Trigger/Ref.',ylabel='Trigger Efficiency')





for trigger in triggers:
  plot_table( sg, mainLogger, trigger, basepath )


triggers = [ 
             "EMU_e28_lhtight_nod0_noringer_ivarloose",
             "EMU_e28_lhtight_nod0_ringer_v6_ivarloose",
             "EMU_e28_lhtight_nod0_ringer_v8_ivarloose",
             ]


eff_et  = [ sg.histogram( basepath+'/'+trigger+'/Efficiency/HLT/eff_et' ) for trigger in triggers ]
eff_eta = [ sg.histogram( basepath+'/'+trigger+'/Efficiency/HLT/eff_eta' ) for trigger in triggers ]
eff_phi = [ sg.histogram( basepath+'/'+trigger+'/Efficiency/HLT/eff_phi' ) for trigger in triggers ]
eff_mu  = [ sg.histogram( basepath+'/'+trigger+'/Efficiency/HLT/eff_mu' ) for trigger in triggers ]
          

legends = ['noringer', 'ringer v6', 'ringer v8']

PlotProfiles( eff_et, legends=legends,runLabel='data18 13TeV', outname='efficiency_v8_data18_13TeV_EGAM1_probes_lhmedium_e28_lhtight_eff_et.pdf',theseColors=theseColors,
              extraText1='e28_lhtight_nod0_ivarloose',doRatioCanvas=False, legendX1=.65, xlabel='E_{T}', rlabel='Trigger/Ref.',ylabel='Trigger Efficiency')

PlotProfiles( eff_eta, legends=legends,runLabel='data18 13TeV', outname='efficiency_v8_data18_13TeV_EGAM1_probes_lhmedium_e28_lhtight_eff_eta.pdf',theseColors=theseColors,
              extraText1='e28_lhtight_nod0_ivarloose',doRatioCanvas=False, legendX1=.65, xlabel='#eta', rlabel='Trigger/Ref.',ylabel='Trigger Efficiency')

PlotProfiles( eff_phi, legends=legends,runLabel='data18 13TeV', outname='efficiency_v8_data18_13TeV_EGAM1_probes_lhmedium_e28_lhtight_eff_phi.pdf',theseColors=theseColors,
              extraText1='e28_lhtight_nod0_ivarloose',doRatioCanvas=False, legendX1=.65, xlabel='#phi', rlabel='Trigger/Ref.',ylabel='Trigger Efficiency')

PlotProfiles( eff_mu, legends=legends,runLabel='data18 13TeV', outname='efficiency_v8_data18_13TeV_EGAM1_probes_lhmedium_e28_lhtight_eff_mu.pdf',theseColors=theseColors,
              extraText1='e28_lhtight_nod0_ivarloose',doRatioCanvas=False, legendX1=.65, xlabel='<#mu>', rlabel='Trigger/Ref.',ylabel='Trigger Efficiency')

eff_et  = [ sg.histogram( basepath+'/'+trigger+'/Efficiency/L2Calo/eff_et' ) for trigger in triggers ]
eff_eta = [ sg.histogram( basepath+'/'+trigger+'/Efficiency/L2Calo/eff_eta' ) for trigger in triggers ]
eff_phi = [ sg.histogram( basepath+'/'+trigger+'/Efficiency/L2Calo/eff_phi' ) for trigger in triggers ]
eff_mu  = [ sg.histogram( basepath+'/'+trigger+'/Efficiency/L2Calo/eff_mu' ) for trigger in triggers ]
 

PlotProfiles( eff_et, legends=legends,runLabel='data18 13TeV', outname='efficiency_v8_data18_13TeV_EGAM1_probes_lhmedium_e28_lhtight_eff_fast_et.pdf',theseColors=theseColors,
              extraText1='e28_lhtight_nod0_ivarloose',doRatioCanvas=False, legendX1=.65, xlabel='E_{T}', rlabel='Trigger/Ref.',ylabel='Trigger Efficiency')

PlotProfiles( eff_eta, legends=legends,runLabel='data18 13TeV', outname='efficiency_v8_data18_13TeV_EGAM1_probes_lhmedium_e28_lhtight_eff_fast_eta.pdf',theseColors=theseColors,
              extraText1='e28_lhtight_nod0_ivarloose',doRatioCanvas=False, legendX1=.65, xlabel='#eta', rlabel='Trigger/Ref.',ylabel='Trigger Efficiency')

PlotProfiles( eff_phi, legends=legends,runLabel='data18 13TeV', outname='efficiency_v8_data18_13TeV_EGAM1_probes_lhmedium_e28_lhtight_eff_fast_phi.pdf',theseColors=theseColors,
              extraText1='e28_lhtight_nod0_ivarloose',doRatioCanvas=False, legendX1=.65, xlabel='#phi', rlabel='Trigger/Ref.',ylabel='Trigger Efficiency')

PlotProfiles( eff_mu, legends=legends,runLabel='data18 13TeV', outname='efficiency_v8_data18_13TeV_EGAM1_probes_lhmedium_e28_lhtight_eff_fast_mu.pdf',theseColors=theseColors,
              extraText1='e28_lhtight_nod0_ivarloose',doRatioCanvas=False, legendX1=.65, xlabel='<#mu>', rlabel='Trigger/Ref.',ylabel='Trigger Efficiency')


for trigger in triggers:
  plot_table( sg, mainLogger, trigger, basepath )





