

#BASEPATH_EGAM1=/afs/cern.ch/work/j/jodafons/public/data17_13TeV/PhysVal_v2/EGAM2/*
BASEPATH_EGAM2=/home/jodafons/cern_data/data/data17_13TeV/PhysVal_v2/EGAM2/*

prun_jobs.py -c "python3 job_collector.py --jpsi" -mt 40 \
	-i /home/jodafons/public/cern_data/data18_13TeV/PhysVal_v2/EGAM2/* 



mkdir data18_EGAM2
rm *.root
mv output* data18_EGAM2





