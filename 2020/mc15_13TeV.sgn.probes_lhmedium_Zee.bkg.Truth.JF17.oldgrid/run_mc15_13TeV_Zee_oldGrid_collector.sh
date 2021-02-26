

BASEPATH_ZEE=~jodafons/public/cern_data/mc15_13TeV/PhysVal_v2/user.jodafons.mc15_13TeV.361106.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Zee.merge.AOD.e3601_s2876_r7917_r7676.PhysVal_v2

prun_jobs.py -i $BASEPATH_ZEE -c "python3 job_collector.py --oldGrid" -mt 40


mkdir mc15_Zee
rm *.root
mv output* mc15_Zee





