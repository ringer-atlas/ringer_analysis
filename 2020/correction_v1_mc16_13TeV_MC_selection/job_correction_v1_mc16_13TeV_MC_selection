from kolmov import  crossval_table, fit_table
import collections
import argparse
import os
parser = argparse.ArgumentParser(description = '', add_help = False)

parser.add_argument('--tunedFiles',action='store', dest='tunedFiles', required=True, help = "path to tuned files (.pic.gz)")
parser.add_argument('--modelTag', action='store', dest='modelTag', required=True, help = "model tag (e.g v1.mc16)")
parser.add_argument('--dataFiles',action='store',dest='dataFiles',required=True, help = "path to npz files")
parser.add_argument('--refFiles', action='store', dest='refFiles', required = True, help = "path to reference files (.ref.pic.gz")
parser.add_argument('--outputPath', action='store', dest='outputPath', required = True, help = "path to the output files")
parser.add_argument('--signature', action='store', dest='signature', required = True, help = "particle signature (Electron, Photon, Muon)")

origin_path = os.getcwd()
etbins = [15,20,30,40,50,100000]
etabins = [0, 0.8 , 1.37, 1.54, 2.37, 2.5]
tuned_info = collections.OrderedDict( {
                  # validation
                  "max_sp_val"      : 'summary/max_sp_val',
                  "max_sp_pd_val"   : 'summary/max_sp_pd_val#0',
                  "max_sp_fa_val"   : 'summary/max_sp_fa_val#0',
                  # Operation
                  "max_sp_op"       : 'summary/max_sp_op',
                  "max_sp_pd_op"    : 'summary/max_sp_pd_op#0',
                  "max_sp_fa_op"    : 'summary/max_sp_fa_op#0',
                  } )

def create_op_dict(op):
    d = {
              op+'_pd_ref'    : "reference/"+op+"_cutbased/pd_ref#0",
              op+'_fa_ref'    : "reference/"+op+"_cutbased/fa_ref#0",
              op+'_sp_ref'    : "reference/"+op+"_cutbased/sp_ref",
              op+'_pd_val'    : "reference/"+op+"_cutbased/pd_val#0",
              op+'_fa_val'    : "reference/"+op+"_cutbased/fa_val#0",
              op+'_sp_val'    : "reference/"+op+"_cutbased/sp_val",
              op+'_pd_op'     : "reference/"+op+"_cutbased/pd_op#0",
              op+'_fa_op'     : "reference/"+op+"_cutbased/fa_op#0",
              op+'_sp_op'     : "reference/"+op+"_cutbased/sp_op",

              # Counts
              op+'_pd_ref_passed'    : "reference/"+op+"_cutbased/pd_ref#1",
              op+'_fa_ref_passed'    : "reference/"+op+"_cutbased/fa_ref#1",
              op+'_pd_ref_total'     : "reference/"+op+"_cutbased/pd_ref#2",
              op+'_fa_ref_total'     : "reference/"+op+"_cutbased/fa_ref#2",
              op+'_pd_val_passed'    : "reference/"+op+"_cutbased/pd_val#1",
              op+'_fa_val_passed'    : "reference/"+op+"_cutbased/fa_val#1",
              op+'_pd_val_total'     : "reference/"+op+"_cutbased/pd_val#2",
              op+'_fa_val_total'     : "reference/"+op+"_cutbased/fa_val#2",
              op+'_pd_op_passed'     : "reference/"+op+"_cutbased/pd_op#1",
              op+'_fa_op_passed'     : "reference/"+op+"_cutbased/fa_op#1",
              op+'_pd_op_total'      : "reference/"+op+"_cutbased/pd_op#2",
              op+'_fa_op_total'      : "reference/"+op+"_cutbased/fa_op#2",
              op+'_op_threshold'     : "reference/"+op+"_cutbased/threshold_op"
    }
    return d

tuned_info = collections.OrderedDict( {
              # validation
              "max_sp_val"      : 'summary/max_sp_val',
              "max_sp_pd_val"   : 'summary/max_sp_pd_val#0',
              "max_sp_fa_val"   : 'summary/max_sp_fa_val#0',
              # Operation
              "max_sp_op"       : 'summary/max_sp_op',
              "max_sp_pd_op"    : 'summary/max_sp_pd_op#0',
              "max_sp_fa_op"    : 'summary/max_sp_fa_op#0',
              } )

tuned_info.update(create_op_dict('tight'))
tuned_info.update(create_op_dict('medium'))
tuned_info.update(create_op_dict('loose'))

args = parser.parse_args()

cv  = crossval_table( tuned_info, etbins = etbins , etabins = etabins )
# cv.fill(args.tunedFiles,args.modelTag)
cv.from_csv('/home/juan.marin/ringer_analysis/2020/crossval_v1_mc16_13TeV_MC_selection/v1.mc16_all_models.csv')
best_inits = cv.filter_inits("max_sp_val")
print(best_inits)
best_inits = best_inits.loc[(best_inits.model_idx==0)]
print(best_inits)
best_sorts = cv.filter_sorts(best_inits, 'max_sp_val')
print(best_sorts)
best_models = cv.get_best_models(best_sorts, remove_last=True)


def generator( path ):
    def norm1( data ):
        norms = np.abs( data.sum(axis=1) )
        norms[norms==0] = 1
        return data/norms[:,None]
    from Gaugi import load
    import numpy as np
    d = load(path)
    feature_names = d['features'].tolist()
    print(path)
    data = norm1(d['data'][:,1:101])
    target = d['target']
    avgmu = d['data'][:,0]
    references = ['T0HLTPhotonT2CaloTight','T0HLTPhotonT2CaloMedium','T0HLTPhotonT2CaloLoose']
    ref_dict={}
    for ref in references:
        answers = d['data'][:, feature_names.index(ref)]
        signal_passed = sum(answers[target==1])
        signal_total = len(answers[target==1])
        background_passed = sum(answers[target==0])
        background_total = len(answers[target==0])
        pd = signal_passed/signal_total
        fa = background_passed/background_total
        ref_dict[ref] = {'signal_passed': signal_passed, 'signal_total': signal_total, 'pd' : pd,
                             'background_passed': background_passed, 'background_total': background_total, 'fa': fa}

    return data, target, avgmu

fileName = os.listdir(args.dataFiles)[0]
model_tag = fileName[0:[n for n in range(len(fileName)) if fileName.find('_et', n) == n][-1]-1]
refName = os.listdir(args.refFiles)[0]
path = args.dataFiles + model_tag + '{ET}_eta{ETA}.npz'
ref_tag = refName[0:[n for n in range(len(fileName)) if fileName.find('_et', n) == n][-1]-1]
# ref_path = args.refFiles + ref_tag + '{ET}_eta{ETA}.ref.pic.gz'
ref_path = '/home/juan.marin/tunings/v1/r0/ref/mc16_13TeV.sgn.MC.gammajet.bkg.vetoMC.dijet.v1_et{ET}_eta{ETA}.ref.pic.gz'

paths = [[ path.format(ET=et,ETA=eta) for eta in range(5)] for et in range(5)]
ref_paths = [[ ref_path.format(ET=et,ETA=eta) for eta in range(5)] for et in range(5)]
ref_matrix = [[ {} for eta in range(5)] for et in range(5)]
references = ['T0HLTPhotonT2CaloTight','T0HLTPhotonT2CaloMedium','T0HLTPhotonT2CaloLoose']
references = ['tight_cutbased', 'medium_cutbased' , 'loose_cutbased']

from saphyra.core import ReferenceReader
for et_bin in range(5):
    for eta_bin in range(5):
        for name in references:
            refObj = ReferenceReader().load(ref_paths[et_bin][eta_bin])
            pd = refObj.getSgnPassed(name)/refObj.getSgnTotal(name)
            fa = refObj.getBkgPassed(name)/refObj.getBkgTotal(name)
            ref_matrix[et_bin][eta_bin][name] = {'pd':pd, 'fa':fa}




# get best models
ct  = fit_table( generator, etbins , etabins, 0.02, 1.5, 16, 40 )
os.chdir(args.outputPath)
os.mkdir(args.outputPath + 'exportToolOutput/')
os.mkdir(args.outputPath + 'exportToolOutput/models')
ct.fill(paths, best_models, ref_matrix,'exportToolOutput/plots')
os.chdir(origin_path)

table = ct.table()
ct.dump_beamer_table(table, best_models, 'test', 'test')
ct.export(best_models, model_tag[0:len(model_tag)-3]+'.model_v1.photonLoose.et%d_eta%d', args.signature+'RingerLooseTriggerConfig.conf', 'loose_cutbased', to_onnx=True)
ct.export(best_models, model_tag[0:len(model_tag)-3]+'.model_v1.photonMedium.et%d_eta%d', args.signature+'RingerMediumTriggerConfig.conf', 'medium_cutbased', to_onnx=True)
ct.export(best_models, model_tag[0:len(model_tag)-3]+'.model_v1.photonTight.et%d_eta%d', args.signature+'RingerTightTriggerConfig.conf', 'tight_cutbased', to_onnx=True)


commandModels = 'mv *.h5 *.json *.onnx ' + args.outputPath + 'exportToolOutput/models'
os.system(commandModels)
commandConf = 'mv *.conf ' + args.outputPath + 'exportToolOutput/'
os.system(commandConf)

