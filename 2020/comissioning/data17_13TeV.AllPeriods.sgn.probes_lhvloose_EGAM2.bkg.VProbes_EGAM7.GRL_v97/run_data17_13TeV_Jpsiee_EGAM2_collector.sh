
prun_jobs.py -c "python3 job_collector.py --jpsi" -mt 1 \
	-i ~/Documents/NeuralRinger/cern_data/PhysVal_v2/data17_13TeV/EGAM2/*



mkdir data17_EGAM2
mv output* data17_EGAM2
rm *.root





