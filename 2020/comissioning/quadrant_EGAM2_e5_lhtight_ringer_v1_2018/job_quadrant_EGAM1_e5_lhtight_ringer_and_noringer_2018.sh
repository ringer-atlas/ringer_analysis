prun_jobs.py -c "python job_quadrant_EGAM1_e5_lhtight_ringer_and_noringer_2018.py --Jpsiee" \
             -i /home/micael/Documents/NeuralRinger/physval_data/data18_13TeV/EGAM2/user.*

mkdir egam2
prun_merge.py -i output_* -o egam2.root -nm 35 -mt 8
mv egam2.root egam2
rm -rf output_*