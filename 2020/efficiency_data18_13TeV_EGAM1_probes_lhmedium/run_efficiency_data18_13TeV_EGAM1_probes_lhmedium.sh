
prun_jobs.py -c "python job_efficiency_data18_13TeV_EGAM1_probes_lhmedium.py" -mt 35  -i ~/public/cern_data/data18_13TeV/PhysVal_v2/EGAM1
mkdir samples
mv *.root samples
prun_merge.py -i samples/*.root -o efficiency_data18_13TeV_EGAM1_vetolhvloose.root -mt 30 -nm 30




