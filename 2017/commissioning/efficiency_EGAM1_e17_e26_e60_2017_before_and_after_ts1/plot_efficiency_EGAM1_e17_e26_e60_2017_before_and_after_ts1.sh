
DATA_2017_BEFORE_TS1="../cern_data/data17_13TeV/Mon/EGAM1/before_ts1/"
DATA_2017_AFTER_TS1="../cern_data/data17_13TeV/Mon/EGAM1/after_ts1/"
#RUNLABEL_1="Data 2017, #int^{}_{}Ldt = 28.7 fb^{-1}"
RUNLABEL_1="Data 2017, #sqrt{s}=13 TeV"


GROUPS="[('HLT_e17_lhvloose_nod0_L1EM15VHI', 'HLT_e26_lhtight_nod0_ivarloose', 'HLT_e60_lhmedium_nod0')]"
EXTRATEXT1="['Full: without ringer', 'Open: with ringer']"
plot_groups.py --groups $GROUPS -t $DATA_2017_AFTER_TS1 -r $DATA_2017_BEFORE_TS1 \
  --pdf_title "Primary triggers, ringer and noringer studies (EGAM1)" \
  --pdf_output "plot_efficiency_EGAM1_e17_e26_e60_2017_before_and_after_ts1.pdf" \
  -o 'plot_efficiency_EGAM1_e17_e26_e60_2017_before_and_after_ts1' \
  --runLabel $RUNLABEL_1 \
  --extraText1 $EXTRATEXT1 \
  #--debug




