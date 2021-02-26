

TRIGGERS="[
'HLT_e17_lhvloose_nod0_L1EM15VHI',
'HLT_e17_lhloose_nod0',
'HLT_e24_lhvloose_nod0_L1EM20VH',
'HLT_e26_lhmedium_nod0',
'HLT_e26_lhtight_nod0_ivarloose',
'HLT_e28_lhtight_nod0_ivarloose',
'HLT_e28_lhtight_nod0_ivarloose_L1EM24VHIM',
'HLT_e60_lhmedium_nod0',
'HLT_e60_lhmedium_nod0_L1EM24VHI',
'HLT_e140_lhloose_nod0',
'HLT_e140_lhloose_nod0_L1EM24VHI',
]"



DATA_2017_AFTER_TS1="../cern_data/data17_13TeV/Mon/EGAM7/after_ts1/"
DATA_2018="../cern_data/data18_13TeV/Mon/EGAM7_merged/"
RUNLABEL="Data 2017, 2018, #sqrt{s}=13 TeV"

plot_triggers.py -d $DATA_2017_AFTER_TS1 $DATA_2018 \
                --triggers $TRIGGERS \
                -l 'data17 (After TS1)' 'data18' \
                -r $RUNLABEL \
                -o 'plot_efficiency_EGAM7_all_triggers_2017_after_ts1_and_2018' \
                --pdf_output 'plot_efficiency_EGAM7_all_triggers_2017_after_ts1_and_2018.pdf' \
                --pdf_title 'Monitoring 2017 and 2018 trigger (EGAM7)' \
                --debug






