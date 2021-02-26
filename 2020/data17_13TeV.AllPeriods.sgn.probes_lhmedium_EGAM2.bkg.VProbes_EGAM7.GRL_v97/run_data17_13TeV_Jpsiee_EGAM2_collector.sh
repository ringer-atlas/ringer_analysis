

#BASEPATH_EGAM1=/afs/cern.ch/work/j/jodafons/public/data17_13TeV/PhysVal_v2/EGAM2/*
BASEPATH_EGAM2=~jodafons/cern_data/data/data17_13TeV/PhysVal_v2/EGAM2/*

prun_jobs.py -i $BASEPATH_EGAM2 -c "python3 job_collector.py --jpsi" -mt 40


mkdir data17_EGAM2
rm *.root
mv output* data17_EGAM2





