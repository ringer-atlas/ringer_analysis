BASEPATH_gammajet=/home/juan.marin/datasets/physval/signal/*

prun_jobs.py -c "python3 job_collector.py --Zrad" -mt 40 -i $BASEPATH_gammajet

mkdir gammajetMC
rm *.root
mv output* gammajetMC