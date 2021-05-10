# EGAM2
prun_jobs.py -c "python3 job_efficiency_v1_data18_13TeV_Jpsiee_probes_lhmedium.py -n 10000" -mt 8 -i ~/Documents/NeuralRinger/cern_data/PhysVal_v2/data18_13TeV/EGAM2/user.*
             
#mkdir egam2
prun_merge.py -i output_* -o test.root -nm 35 -mt 8
#mv egam2.root egam2
rm -rf output_*

# EGAM7
#prun_jobs.py -c "python3 job_efficiency_v1_data18_13TeV_Jpsiee_probes_lhmedium.py --fake" -mt 8 -i ~/Documents/NeuralRinger/cern_data/PhysVal_v2/data18_13TeV/EGAM7/user.*

#mkdir EGAM7
#prun_merge.py -i output_* -o egam7.root -nm 35 -mt 8
#mv egam7.root EGAM7
#rm -rf output_*