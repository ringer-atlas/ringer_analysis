# EGAM2
prun_jobs.py -c "python3 job_efficiency_v1_data17_13TeV_Jpsiee_probes_lhloose.py" -mt 8 -i ~/Documents/NeuralRinger/cern_data/PhysVal_v2/data17_13TeV/EGAM2/user.*
             
mkdir data17_egam2_lhloose
prun_merge.py -i output_* -o data17_egam2_lhloose.root -nm 35 -mt 8
mv data17_egam2_lhloose.root data17_egam2_lhloose
rm -rf output_*

# EGAM7
prun_jobs.py -c "python3 job_efficiency_v1_data17_13TeV_Jpsiee_probes_lhloose.py --fake" -mt 8 -i ~/Documents/NeuralRinger/cern_data/PhysVal_v2/data17_13TeV/EGAM7/before_ts1/user.*

mkdir data17_before_ts1_egam7_lhloose
prun_merge.py -i output_* -o data17_before_ts1_egam7_lhloose.root -nm 35 -mt 8
mv data17_before_ts1_egam7_lhloose.root data17_before_ts1_egam7_lhloose
rm -rf output_*

# EGAM7
prun_jobs.py -c "python3 job_efficiency_v1_data17_13TeV_Jpsiee_probes_lhloose.py --fake" -mt 8 -i ~/Documents/NeuralRinger/cern_data/PhysVal_v2/data17_13TeV/EGAM7/after_ts1/user.*

mkdir data17_after_ts1_egam7_lhloose
prun_merge.py -i output_* -o data17_after_ts1_egam7_lhloose.root -nm 35 -mt 8
mv data17_after_ts1_egam7_lhloose.root data17_after_ts1_egam7_lhloose
rm -rf output_*