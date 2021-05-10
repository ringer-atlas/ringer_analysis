from Gaugi.messenger import LoggingLevel, Logger
from Gaugi.storage import restoreStoreGate
#from EfficiencyTools import PlotProfiles, GetProfile
from EfficiencyTools import GetProfile
from old_plot_profiles import PlotProfiles

import ROOT

ROOT.gROOT.SetBatch(True)

mainLogger = Logger.getModuleLogger("job")
mainLogger.level = LoggingLevel.INFO

theseColors = [ROOT.kBlack, ROOT.kGray+2, ROOT.kBlue-2, ROOT.kBlue-4]

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


def get( sg, path, histname, resize=None ):
  return GetProfile( sg.histogram( path + '/match_'+histname), sg.histogram( path + '/' + histname ), resize=resize )



inputFile = 'data17_before_ts1_egam7_lhloose/data17_before_ts1_egam7_lhloose.root'
basepath = 'Event/EfficiencyTool'

sg =  restoreStoreGate( inputFile )

chain_dict_config = {
  'HLT_e7_lhvloose_nod0' : {
                            'triggers' : ["EMU_e7_lhvloose_nod0_noringer", "EMU_e7_lhvloose_nod0_ringer_v1",],
                            'plotname' : 'efficiency_v1_data18_13TeV_%s_%s_e5_lhvloose_nod0_eff',
                            },
  'HLT_e9_lhvloose_nod0' : {
                            'triggers' : ["EMU_e9_lhvloose_nod0_noringer", "EMU_e9_lhvloose_nod0_ringer_v1",],
                            'plotname' : 'efficiency_v1_data18_13TeV_%s_%s_e5_lhvloose_nod0_eff',
                            },
  'HLT_e12_lhvloose_nod0' : {
                            'triggers' : ["EMU_e12_lhvloose_nod0_noringer", "EMU_e12_lhvloose_nod0_ringer_v1",],
                            'plotname' : 'efficiency_v1_data18_13TeV_%s_%s_e5_lhvloose_nod0_eff',
                            },
  'HLT_e5_lhvloose_nod0' : {
                            'triggers' : ["EMU_e5_lhvloose_nod0_noringer", "EMU_e5_lhvloose_nod0_ringer_v1",],
                            'plotname' : 'efficiency_v1_data18_13TeV_%s_%s_e5_lhvloose_nod0_eff',
                            },
  'HLT_e5_lhloose_nod0'  : {
                            'triggers' : ["EMU_e5_lhloose_nod0_noringer", "EMU_e5_lhloose_nod0_ringer_v1",],
                            'plotname' : 'efficiency_v1_data18_13TeV_%s_%s_e5_lhloose_nod0_eff',
                            },
  'HLT_e5_lhmedium_nod0' : {
                            'triggers' : ["EMU_e5_lhmedium_nod0_noringer", "EMU_e5_lhmedium_nod0_ringer_v1",],
                            'plotname' : 'efficiency_v1_data18_13TeV_%s_%s_e5_lhmedium_nod0_eff',
                            },
  'HLT_e5_lhtight_nod0'  : {
                            'triggers' : ["EMU_e5_lhtight_nod0_noringer", "EMU_e5_lhtight_nod0_ringer_v1",],
                            'plotname' : 'efficiency_v1_data18_13TeV_%s_%s_e5_lhtight_nod0_eff',
                            },

  'HLT_e7_lhmedium_nod0' : {
                            'triggers' : ["EMU_e7_lhmedium_nod0_noringer", "EMU_e7_lhmedium_nod0_ringer_v1",],
                            'plotname' : 'efficiency_v1_data18_13TeV_%s_%s_e7_lhmedium_nod0_eff',
                            },
  'HLT_e9_lhloose_nod0'  : {
                            'triggers' : ["EMU_e9_lhloose_nod0_noringer", "EMU_e9_lhloose_nod0_ringer_v1",],
                            'plotname' : 'efficiency_v1_data18_13TeV_%s_%s_e9_lhloose_nod0_eff',
                            },
  'HLT_e9_lhmedium_nod0' : {
                            'triggers' : ["EMU_e9_lhmedium_nod0_noringer", "EMU_e9_lhmedium_nod0_ringer_v1",],
                            'plotname' : 'efficiency_v1_data18_13TeV_%s_%s_e9_lhmedium_nod0_eff',
                            },
  'HLT_e9_lhtight_nod0'  : {
                            'triggers' : ["EMU_e9_lhtight_nod0_noringer", "EMU_e9_lhtight_nod0_ringer_v1",],
                            'plotname' : 'efficiency_v1_data18_13TeV_%s_%s_e9_lhtight_nod0_eff',
                            }, 
  'HLT_e12_lhmedium_nod0' : {
                            'triggers' : ["EMU_e12_lhmedium_nod0_noringer", "EMU_e12_lhmedium_nod0_ringer_v1",],
                            'plotname' : 'efficiency_v1_data18_13TeV_%s_%s_e12_lhmedium_nod0_eff',
                            },
}


for ichain in chain_dict_config.keys():
  triggers = chain_dict_config[ichain]['triggers']
  print('Chain: %s' %(ichain))
  for istep in ['L2Calo', 'HLT']:
    plotname = chain_dict_config[ichain]['plotname'] %(inputFile.split('/')[0], istep)
          
    eff_et  = [ get(sg, basepath+'/'+trigger+'/Efficiency/%s'%(istep), 'et') for trigger in triggers ]
    eff_eta = [ get(sg, basepath+'/'+trigger+'/Efficiency/%s'%(istep), 'eta') for trigger in triggers ]
    eff_phi = [ get(sg, basepath+'/'+trigger+'/Efficiency/%s'%(istep), 'phi') for trigger in triggers ]
    eff_mu  = [ get(sg, basepath+'/'+trigger+'/Efficiency/%s'%(istep), 'mu', [8,20,60]) for trigger in triggers ]
    
    legends = ['noringer', 'ringer v1']#, 'ringer old v1', 'ringer old v1 2']


  for trigger in triggers:
    plot_table( sg, mainLogger, trigger, basepath )
'''
    PlotProfiles( eff_et, legends=legends,runLabel='data18 13TeV', outname='%s_et.pdf' %(plotname), theseColors=theseColors,
                  extraText1=ichain,doRatioCanvas=False, legendX1=.65, xlabel='E_{T}', rlabel='Trigger/Ref.',ylabel='Trigger Efficiency')

    PlotProfiles( eff_eta, legends=legends,runLabel='data18 13TeV', outname='%s_eta.pdf' %(plotname),theseColors=theseColors,
                  extraText1=ichain, doRatioCanvas=False, legendX1=.65, xlabel='#eta', rlabel='Trigger/Ref.',ylabel='Trigger Efficiency')

    PlotProfiles( eff_phi, legends=legends,runLabel='data18 13TeV', outname='%s_phi.pdf' %(plotname),theseColors=theseColors,
                  extraText1=ichain, doRatioCanvas=False, legendX1=.65, xlabel='#phi', rlabel='Trigger/Ref.',ylabel='Trigger Efficiency')

    PlotProfiles( eff_mu, legends=legends,runLabel='data18 13TeV', outname='%s_mu.pdf' %(plotname),theseColors=theseColors,
                  extraText1=ichain, doRatioCanvas=False, legendX1=.65, xlabel='<#mu>', rlabel='Trigger/Ref.',ylabel='Trigger Efficiency')
'''

