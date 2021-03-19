import os
import re
import sys
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Gaugi import load
import collections

from kolmov import *
from itertools import product


import argparse
  


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
    }
    return d


parser = argparse.ArgumentParser(description = '', add_help = False)

parser.add_argument('-i','--inputTable', action='store',
    dest='inputTable', required = False, nargs='+',
    help = "The csv table input (all models)")

parser.add_argument('-o','--outputPath', action='store',
    dest='outputPath', required = False, nargs='+',
    help = "output Path")
args = parser.parse_args()


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

zrad_et_lims    = [15,20,30,40,50,1000000]
eta_lims       = [0, 0.8 , 1.37, 1.54, 2.37, 2.5]
cv = crossval_table( tuned_info, etbins = zrad_et_lims, etabins = eta_lims )
cv.from_csv(args.inputTable[0])
best_inits = cv.filter_inits("max_sp_val")
n_min, n_max = 2, 5
model_add_tag = { idx : '.mlp%i' %(neuron) for idx, neuron in enumerate(range(n_min, n_max +1))}
best_inits.train_tag = best_inits.train_tag + best_inits.model_idx.replace(model_add_tag)
best_inits.shape, best_inits.model_idx.nunique()*25*10
os.chdir(args.outputPath[0])
for et in range(5):
  for eta in range(5):

    best_inits_fixed_bin = best_inits.loc[(best_inits.train_tag== 'v1.mc16' + '.mlp5') & (best_inits.et_bin == et) & (best_inits.eta_bin == eta)]
    colors = ['blue','darkblue','red','darkred','yellow','orange','purple','black','green','magenta']
    for i,sort in enumerate(best_inits_fixed_bin.sort):
      df_sort = best_inits_fixed_bin.loc[best_inits_fixed_bin.sort == sort]
      path = df_sort.file_name.values[0]
      history = load( path)['tunedData'][0]['history']
      pd, fa = history['summary']['rocs']['roc_val']
      fa_val = history['reference']['medium_cutbased']['fa_val'][0]
      pd_val = history['reference']['medium_cutbased']['pd_val'][0]
      plt.plot( fa, pd, linewidth=2, color=colors[i])
      plt.plot( fa_val, pd_val, linewidth=2, color=colors[i], marker='*', markersize=12, label='sort_'+str(sort))
      plt.xlim(0,1)
      plt.ylim(0,1)
      plt.legend(loc='best')

    plt.xlabel('Fake Probability [%]')
    plt.ylabel('Detection Probability [%]')

    ax2 = plt.gca().twinx()
    for i,sort in enumerate(best_inits_fixed_bin.sort):
      df_sort = best_inits_fixed_bin.loc[best_inits_fixed_bin.sort == sort]
      path = df_sort.file_name.values[0]
      history = load( path)['tunedData'][0]['history']
      fa_val = history['reference']['medium_cutbased']['fa_val'][0]
      thr_val = history['reference']['medium_cutbased']['threshold_val']
      ax2.plot( fa_val, thr_val, color=colors[i], marker='o', markersize=8)

    ax2.set_ylim(-1,1)
    ax2.set_ylabel('Threshold',labelpad=1)
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    ax2.text(0.4, 0.05, 'Circles - Respective Threshold Value', transform=ax2.transAxes, fontsize=10, verticalalignment='top', bbox=props)

    etmin = zrad_et_lims[et]
    etmax = zrad_et_lims[et+1]
    etamin = eta_lims[eta]
    etamax = eta_lims[eta+1]
    if et < 4:
      plt.title(str(etamin) + "<" + r'$\eta $' +"<" + str(etamax) + " -  " + str(etmin) + "< " + r'$E_T $'+ " < " + str(etmax) + " GeV")
    else:
      plt.title(str(etamin) + "<" + r'$\eta $' +"<" + str(etamax) + " -  "  + r'$E_T $'+ " > " + str(etmin) + " GeV")


    plt.savefig('roc_curve_et_'+str(et) + '_eta'+str(eta) + '_mlp5_fa_threshold.png')
    print('Saving roc_curve_et_'+str(et) + '_eta'+str(eta) + '_mlp5_fa_threshold.png ......')
    plt.close()