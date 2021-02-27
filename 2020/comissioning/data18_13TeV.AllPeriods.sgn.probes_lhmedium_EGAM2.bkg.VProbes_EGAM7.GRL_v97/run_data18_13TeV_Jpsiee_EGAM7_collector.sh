

BASEPATH_EGAM7=/home/jodafons/public/cern_data/data18_13TeV/PhysVal_v2/EGAM7/*

prun_jobs.py -i $BASEPATH_EGAM7 -c "python3 job_collector.py --jpsi --egam7" -mt 40


mkdir data18_EGAM7
rm *.root
mv output* data18_EGAM7





