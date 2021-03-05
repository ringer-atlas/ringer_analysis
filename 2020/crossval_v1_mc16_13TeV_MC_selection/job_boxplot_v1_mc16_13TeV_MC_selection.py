import os
import re
import sys
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

def create_cool_box_plot(df, key, mapped_key, output_name, tuning_flag):
    # create the box plot. 
    # rename the columns names.
    # map the model idx into real # neurons.
	sns.catplot(data=(df.replace({	'model_idx' : {i :  n for i, n in zip(range(0,9),range(2,10+1))},
	                          			'et_bin'    : {i : str_etbins_zee[i] for i in range(5)},
	                          			'eta_bin'   : {i : str_etabins[i] for i in range(5)}}).rename({'model_idx'  : '# Neurons','et_bin': r'$E_T$', 'eta_bin' : r'$\eta$', 
	                          			key : mapped_key},	axis=1)), 
				x='# Neurons',
	            y=mapped_key, 
	            col=r'$\eta$', 
	            row=r'$E_T$', 
	            kind='box' )
	
	plt.savefig('box_plot_%s_%s.png' %(output_name, tuning_flag), dpi=300)
	plt.close()


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
cv.from_csv('v1.mc16_all_models.csv')
best_inits = cv.filter_inits("max_sp_val")

best_inits.head()

n_min, n_max = 2, 5
model_add_tag = { idx : '.mlp%i' %(neuron) for idx, neuron in enumerate(range(n_min, n_max +1))}
best_inits.train_tag = best_inits.train_tag + best_inits.model_idx.replace(model_add_tag)
best_inits.shape, best_inits.model_idx.nunique()*25*10


best_inits = best_inits.loc[(best_inits.train_tag== 'v1.mc16' + '.mlp2')  |
                            (best_inits.train_tag== 'v1.mc16' + '.mlp3')  |
                            (best_inits.train_tag== 'v1.mc16' + '.mlp4')  |
                            (best_inits.train_tag== 'v1.mc16' + '.mlp5')  ]


map_key_dict ={
   'max_sp_val'    : (r'$SP_{max}$ (Validation)', 'sp'),
   'max_sp_pd_val' : (r'$P_D$ (Validation)', 'pd'),
   'max_sp_fa_val' : (r'$F_A$ (Validation)', 'fa'),
   'auc_val'       : (r'AUC (Validation)', 'auc'),
}
ikey         = 'max_sp_val'
map_k, o_name = map_key_dict[ikey]
best_inits.to_csv('v1.mc16_best_init.csv', index=False)

create_cool_box_plot(df=best_inits, key=ikey, mapped_key=map_k, output_name=o_name, tuning_flag='v1.mc16.all_neurons')

best_sorts = cv.filter_sorts(best_inits,'max_sp_op')
best_sorts.to_csv('v1.mc16_best_sorts.csv', index=False)

cv.plot_roc_curves( best_sorts = best_inits, legends=['k0','k1','k2','k3'], et_bin = 0, eta_bin = 4,
                        output='rocs_v1.pdf',display=False, colors=get_color_fader('blue','red',6), tags=['v1.mc16.mlp2'])

cv.plot_training_curves(best_inits, best_sorts, 'v1.mc16')