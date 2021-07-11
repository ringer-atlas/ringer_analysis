

#BASEPATH_EGAM1=/afs/cern.ch/work/j/jodafons/public/data17_13TeV/PhysVal_v2/EGAM7/*
BASEPATH_EGAM7=~jodafons/public/cern_data/data17_13TeV/PhysVal_v2/EGAM7/*

prun_jobs.py -i $BASEPATH_EGAM7 -c "python3 job_collector.py --oldPath --egam7" -mt 40


mkdir data17_EGAM7
rm *.root
mv output* data17_EGAM7











