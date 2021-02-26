

TRIGGERS="[
('HLT_e28_lhtight_nod0_ivarloose','HLT_e28_lhtight_nod0_noringer_ivarloose'),
]"



DATA_2017_AFTER_TS1="/Volumes/castor/cern_data/data17_13TeV/Mon/EGAM7/after_ts1/"
RUNLABEL="Data 2017, #sqrt{s}=13 TeV"
EXTRATEXT1="['e28_lhtight_nod0_ivarloose']"
plot_groups.py  -t $DATA_2017_AFTER_TS1 \
                --groups $TRIGGERS \
                -l 'With Ringer (Ref.)' 'Without Ringer' \
                --runLabel $RUNLABEL \
                --extraText1 $EXTRATEXT1 \
                -o 'plot_efficiency_EGAM7_e28_ringer_and_noringer_2017_after_ts1' \
                --pdf_output 'plot_efficiency_EGAM7_e28_ringer_and_noringer_2017_after_ts1.pdf' \
                --pdf_title 'Monitoring 2017 With/Without Ringer (EGAM7, After TS1)'









