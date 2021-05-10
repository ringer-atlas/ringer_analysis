prun_jobs.py -c "python job_quadrant_EGAM2_e5_lh_all_ringer_and_noringer.py --Jpsiee" -i ~/Documents/NeuralRinger/cern_data/PhysVal_v2/data18_13TeV/EGAM2/user.* -mt 6

mkdir egam2
prun_merge.py -i output_* -o egam2.root -nm 35 -mt 8
mv egam2.root egam2
rm -rf output_*