
prun_jobs.py -c "python job_impact_EGAM2_e5_lhtight_ringer.py --Jpsiee" \
             -i /home/micael/Documents/NeuralRinger/physval_data/data18_13TeV/EGAM2/user.*


mkdir calib_kl_egam2
prun_merge.py -i output_* -o egam2.root -nm 35 -mt 8
mv egam2.root calib_kl_egam2
rm -rf output_*








