

BASEPATH_JF17=~jodafons/public/cern_data/mc15_13TeV/PhysVal_v2/user.jodafons.mc15_13TeV.423300.Pythia8EvtGen_A14NNPDF23LO_perf_JF17.merge.AOD.e3848_s2876_r7917_r7676.PhysVal_v2

prun_jobs.py -i $BASEPATH_JF17 -c "python3 job_collector.py --jf17 --oldGrid" -mt 40


mkdir mc15_JF17
rm *.root
mv output* mc15_JF17





