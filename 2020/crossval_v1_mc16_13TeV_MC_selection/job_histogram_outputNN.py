from tensorflow.keras.models import Model, model_from_json
from Gaugi import load
import json
import numpy as np
import matplotlib.pyplot as plt
from kolmov import *
import pandas as pd

def norm1( data ):
    norms = np.abs( data.sum(axis=1) )
    norms[norms==0] = 1
    return data/norms[:,None]

def plotSingleHistogram(et, eta, model_idx, df, data, sort):

	dataPath = data
	m_df = pd.read_csv(df) 
	if sort:
		m_model_info = m_df.loc[(m_df.et_bin == et ) & (m_df.eta_bin == eta) & (m_df.model_idx == model_idx) & (m_df.sort == sort-1)] 
	else:
		m_model_info = m_df.loc[(m_df.et_bin == et ) & (m_df.eta_bin == eta) & (m_df.model_idx == model_idx)] 
	path = m_model_info.file_name.values[0]

	tuned = load(path)['tunedData'][0]
	tunedModel = model_from_json( json.dumps(tuned['sequence'], separators=(',', ':')) )
	tunedModel.set_weights( tuned['weights'] )

	
	inputFile = np.load(dataPath)
	data = inputFile['data']
	target = inputFile['target']
	sgnRings=data[target == 1, 1:101] 
	bkgRings=data[target != 1, 1:101] 

	sgnPredict = tunedModel.predict(norm1(sgnRings))
	bkgPredict = tunedModel.predict(norm1(bkgRings))
	from ROOT import TH1F, TCanvas, TPaveText, kBlue, kRed, kGreen, gPad, gStyle, TLine, TLegend, THStack

	sgnHist = TH1F('signal','signal',100,-1,1)
	bkgHist = TH1F('background','background',100,-1,1)

	for sgn in sgnPredict:
	    sgnHist.Fill(sgn)

	for bkg in bkgPredict:
	    bkgHist.Fill(bkg)

	sgnHist.SetLineColor(kBlue)
	sgnHist.SetFillStyle(3444)
	sgnHist.SetFillColorAlpha(kBlue,0.5)
	bkgHist.SetFillColorAlpha(kRed,0.5)
	bkgHist.SetFillStyle(3444)
	bkgHist.SetLineColor(kRed)
	c = TCanvas('c','c',500,500)

	etmin = etbins_values[et]
	etmax = etbins_values[et+1]
	etamin = etabins_values[eta]
	etamax = etabins_values[eta+1]
	hstack = THStack('hs','')
	hstack.Add(sgnHist)
	hstack.Add(bkgHist)
	hstack.Draw('nostack')
	hstack.GetXaxis().SetTitle('NN Output')
	hstack.GetYaxis().SetTitle("Counts")
	
	if et < 4:
		hstack.SetTitle("Sort " +str(sort-1) +" Histogram - " + str(etamin) + " < #eta < " + str(etamax) + " -  " + str(etmin) + "< E_{T} < " + str(etmax) + " GeV")
	else:
		hstack.SetTitle("Sort " +str(sort-1) +" Histogram - " + str(etamin) + " < #eta < " + str(etamax) + " -  " " E_{T} > " + str(etmin)   + " GeV")
	c.Update()
	text = TPaveText(0.22,hstack.GetMaximum(),0.9,hstack.GetMaximum() - 0.15*hstack.GetMaximum())
	threshold = tuned['history']['reference']['medium_cutbased']['threshold_val']
	pd_op = tuned['history']['reference']['medium_cutbased']['pd_val'][0]*100
	fa_op = tuned['history']['reference']['medium_cutbased']['fa_val'][0]*100
	sp_op = tuned['history']['reference']['medium_cutbased']['sp_val']*100
	text.AddText("Probability Detection: " + str(round(pd_op,2)) + "%")
	text.AddText("False Alarm: " + str(round(fa_op,2)) + "%")
	text.AddText("SP index: " + str(round(sp_op,2)) + "%")
	text.AddText("Threshold: " + str(round(threshold,2)))
	text.SetTextSize(0.02)
	legend = TLegend(0.22,0.71,0.48,0.8);
	legend.AddEntry(sgnHist,"Signal Histogram","f");
	legend.AddEntry(bkgHist,"Background Histogram", "f");
	text.Draw()
	c.Update()
	c.SetLogy()
	line = TLine(threshold,gPad.GetUymin(),threshold,gPad.GetUymax())
	line.SetLineColor(kGreen+3)
	line.SetLineWidth(5)
	line.SetLineStyle(10)
	line.Draw('sames')
	legend.AddEntry(line,"Threshold","l");
	legend.Draw('sames')
	gStyle.SetOptStat(0)
	if (sort):
		c.SaveAs('histogram_et' + str(et) + '_eta' + str(eta) + '_mlp'+str(model_idx + 2) + '_sort_' + str(sort-1) + '.pdf')
		print('Saving histogram_et' + str(et) + '_eta' + str(eta) + '_mlp'+str(model_idx + 2) + '_sort_' + str(sort-1) + '.pdf .........')
	else:
		c.SaveAs('histogram_et' + str(et) + '_eta' + str(eta) + '_mlp'+str(model_idx + 2) + '.pdf')
		print('Saving histogram_et' + str(et) + '_eta' + str(eta) + '_mlp'+str(model_idx + 2) + '.pdf .........')




import argparse
import os

parser = argparse.ArgumentParser(description = '', add_help = False)

parser.add_argument('-i','--inputFiles', action='store',
    dest='inputFiles', required = False, nargs='+',
    help = "The npz input files that will be used")

parser.add_argument('-it','--bestInitTable', action='store',
    dest='bestInitTable', required = False, default = None,
    help = "The CSV table (best_inits).")

parser.add_argument('-st','--bestSortTable', action='store',
    dest='bestSortTable', required = False, default = None,
    help = "The CSV table (best_sorts).")

parser.add_argument('-h','--hiddenNeurons', action='store',
    dest='hiddenNeurons', required = False, default = None,
    help = "The CSV table.")

parser.add_argument('-o','--outputPath', action='store',
    dest='outputPath', required = False, default = None,
    help = "The output store path.")

etbins_values = [15, 20, 30, 40, 50, 100000]
etabins_values = [0, 0.8, 1.37, 1.54, 2.37, 2.50]

args = parser.parse_args()
os.chdir(args.outputPath)

if args.bestSortTable:
	for etBin in range(5):
		for etaBin in range(5):
			plotSingleHistogram(et=etBin,eta=etaBin,model_idx=int(args.hiddenNeurons) - 2, df = args.bestSortTable, data = args.inputFiles[0]+str(etBin) + '_eta'+str(etaBin)+'.npz', sort=False)

elif args.bestInitTable:
	for etBin in range(5):
		for etaBin in range(5):
			try:
				os.mkdir(args.outputPath+'sort_separation_histogram_et_'+str(etBin)+'_eta_'+str(etaBin))
				os.chdir(args.outputPath+'sort_separation_histogram_et_'+str(etBin)+'_eta_'+str(etaBin))
			except:
				os.chdir(args.outputPath+'sort_separation_histogram_et_'+str(etBin)+'_eta_'+str(etaBin))
			for sort in range(10):
				plotSingleHistogram(et=etBin,eta=etaBin,model_idx=int(args.hiddenNeurons) - 2, df = args.bestInitTable, data = args.inputFiles[0]+str(etBin) + '_eta'+str(etaBin)+'.npz', sort=sort+1)
else:
	for etBin in range(5):
		for etaBin in range(5):
			plotSingleHistogram(et=etBin,eta=etaBin,model_idx=int(args.hiddenNeurons) - 2, df = args.bestSortTable, data = args.inputFiles[0]+str(etBin) + '_eta'+str(etaBin)+'.npz', sort=False)