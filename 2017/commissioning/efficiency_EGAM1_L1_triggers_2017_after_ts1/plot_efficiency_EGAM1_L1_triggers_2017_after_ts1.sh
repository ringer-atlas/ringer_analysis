

TRIGGERS="[
('L1_EM15VH','L1_EM15VHI','L1_EM20VH','L1_EM20VHI','L1_EM22VHI','L1_EM24VHI'),
]"

#DATA_2017_BEFORE_TS1="cern_data/data17_13TeV/Mon/EGAM1_L1_only/before_ts1/"
DATA_2017_AFTER_TS1="../cern_data/data17_13TeV/Mon/EGAM1_L1_only/after_ts1/"
RUNLABEL="Data 2017, #sqrt{s}=13 TeV"
EXTRATEXT1="'Z#rightarrow ee, T&P'"

plot_groups.py  -t $DATA_2017_AFTER_TS1 \
                --groups $TRIGGERS \
                -l 'EM15VH' 'EM15VHI' 'EM20VH' 'EM20VHI' 'EM22VHI' 'EM24VHI' \
                --runLabel $RUNLABEL \
                --extraText1 $EXTRATEXT1 \
                -o 'plot_efficiency_EGAM1_L1_triggers_2017_after_ts1' \
                --pdf_output 'plot_efficiency_EGAM1_L1_triggers_2017_after_ts1.pdf' \
                --pdf_title 'Monitoring 2017 (EGAM1, After TS1)'









