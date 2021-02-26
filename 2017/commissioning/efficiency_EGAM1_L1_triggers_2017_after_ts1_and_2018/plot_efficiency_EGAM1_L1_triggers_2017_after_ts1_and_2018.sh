


TRIGGERS="[
('L1_EM15VH','L1_EM15VHI','L1_EM20VH','L1_EM20VHI','L1_EM22VHI','L1_EM24VHI'),
]"

#TRIGGERS="[
#('L1_EM15VH','L1_EM22VHI','L1_EM24VHI'),
#]"




DATA_2017_AFTER_TS1="../cern_data/data17_13TeV/Mon/EGAM1_L1_only/after_ts1/"
DATA_2018="../cern_data/data18_13TeV/Mon/EGAM1_L1_only/"
RUNLABEL="Data 2017,2018, #sqrt{s}=13 TeV"

EXTRATEXT1="'2017 (after TS1) and 2018'"

plot_groups.py  -r $DATA_2017_AFTER_TS1 \
                -t $DATA_2018 \
                --groups $TRIGGERS \
                -l 'EM15VH' 'EM15VHI' 'EM22VHI'  'EM20VH' 'EM22VHI' 'EM24VHI' \
                --runLabel $RUNLABEL \
                -o 'plot_efficiency_EGAM1_L1_triggers_2017_after_ts1_and_2018' \
                --pdf_output 'plot_efficiency_EGAM1_L1_triggers_2017_after_ts1_and_2018.pdf' \
                --pdf_title 'Monitoring 2017 and 2018 (EGAM1)'
                #--extraText1 $EXTRATEXT1 \








