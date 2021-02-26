

#BASEPATH_EGAM1=/afs/cern.ch/work/j/jodafons/public/data17_13TeV/PhysVal_v2/EGAM1/*
BASEPATH_EGAM1=~jodafons/public/cern_data/data17_13TeV/PhysVal_v2/EGAM1/*

prun_jobs.py -i $BASEPATH_EGAM1 -c "python3 job_collector.py --oldPath" -mt 40


mkdir data17_EGAM1
rm *.root
mv output* data17_EGAM1





