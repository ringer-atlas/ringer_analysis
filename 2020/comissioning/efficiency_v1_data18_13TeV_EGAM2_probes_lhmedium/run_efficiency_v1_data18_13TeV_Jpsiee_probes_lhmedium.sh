# EGAM2
prun_jobs.py -c "python3 job_efficiency_v1_data18_13TeV_Jpsiee_probes_lhmedium.py"\
             -mt 8 \
             -i /home/micael/Documents/NeuralRinger/physval_data/data18_13TeV/EGAM2/user.*
#             -i /home/micael/Documents/NeuralRinger/physval_data/data18_13TeV/EGAM2/user.jodafons.data18_13TeV.periodB.physics_Main.PhysCont.DAOD_EGAM2.grp18_v01_p3628.physval.Grl_v102_GLOBAL/user.jodafons.17184393.GLOBAL._000014.root
             

#mkdir EGAM2
prun_merge.py -i output_* -o sk_egam2.root -nm 35 -mt 8
#mv egam2.root EGAM2
rm -rf output_*

# EGAM7
#prun_jobs.py -c "python3 job_efficiency_v1_data18_13TeV_Jpsiee_probes_lhmedium.py --fake"\
#             -mt 8 \
#             -i /home/micael/Documents/NeuralRinger/physval_data/data18_13TeV/EGAM7/user.*


#mkdir EGAM7
#prun_merge.py -i output_* -o egam7.root -nm 35 -mt 8
#mv egam7.root EGAM7
#rm -rf output_*