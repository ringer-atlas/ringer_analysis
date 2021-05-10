# egam2 data 18
prun_jobs.py -c "python job_impact_EGAM2_e5_lhtight_ringer.py --Jpsiee" -i ~/Documents/NeuralRinger/cern_data/PhysVal_v2/data18_13TeV/EGAM2/user.*

mkdir impact_egam2_medium_data18
prun_merge.py -i output_* -o impact_egam2.root -nm 5 -mt 4
mv impact_egam2.root impact_egam2_medium_data18
rm -rf output_*

# egam7 data 18
#prun_jobs.py -c "python job_impact_EGAM2_e5_lhtight_ringer.py --Jpsiee --egam7" -i ~/Documents/NeuralRinger/cern_data/PhysVal_v2/data18_13TeV/EGAM7/user.*

#mkdir impact_egam7_no_pid_data18
#prun_merge.py -i output_* -o impact_egam7.root -nm 2 -mt 6
#mv impact_egam7.root impact_egam7_no_pid_data18
#rm -rf output_*

## data 17
#prun_jobs.py -c "python job_impact_EGAM2_e5_lhtight_ringer.py --Jpsiee" -i ~/Documents/NeuralRinger/cern_data/PhysVal_v2/data17_13TeV/EGAM2/user.*
#
#mkdir impact_egam2_no_pid_data17
#prun_merge.py -i output_* -o impact_egam2.root -nm 5 -mt 4
#mv impact_egam2.root impact_egam2_no_pid_data17
#rm -rf output_*









