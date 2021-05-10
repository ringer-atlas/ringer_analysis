

#BASEPATH_EGAM7=/afs/cern.ch/work/j/jodafons/public/data17_13TeV/PhysVal_v2/EGAM7/*
BASEPATH_EGAM7=~/Documents/NeuralRinger/cern_data/PhysVal_v2/data17_13TeV/EGAM7/*

prun_jobs.py -i $BASEPATH_EGAM7 -c "python3 job_collector.py --jpsi --egam7 --oldPath" -mt 40


mkdir data17_EGAM7
mv output* data17_EGAM7
rm *.root





