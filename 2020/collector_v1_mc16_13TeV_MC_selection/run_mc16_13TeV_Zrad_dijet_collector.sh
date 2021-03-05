BASEPATH_dijet = /home/juan.marin/datasets/physval/background/*

prun_jobs.py -c "python3 job_collector.py --fakes" -mt 40 -i BASEPATH_dijet


mkdir dijetMC
rm *.root
mv output* dijetMC