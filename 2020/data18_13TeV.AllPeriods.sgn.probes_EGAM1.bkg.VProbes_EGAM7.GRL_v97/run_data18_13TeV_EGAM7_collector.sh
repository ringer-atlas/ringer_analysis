

#BASEPATH_EGAM1=/afs/cern.ch/work/j/jodafons/public/data17_13TeV/PhysVal_v2/EGAM7/*
BASEPATH_EGAM7=~jodafons/public/cern_data/data18_13TeV/PhysVal_v2/EGAM7/*

prun_jobs.py -i $BASEPATH_EGAM7 -c "python3 job_collector.py --egam7" -mt 40


mkdir data18_EGAM7
rm *.root
mv output* data18_EGAM7











