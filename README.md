
# The ringer analysis repository

In 2017 the ATLAS experiment implemented an ensemble of neural networks
(NeuralRinger algorithm) dedicated to improving the performance of filtering
events containing electrons in the high-input rate online environment of the
Large Hadron Collider at CERN, Geneva. The ensemble employs a concept of
calorimetry rings. The training procedure and final structure of the ensemble
are used to minimize fluctuations from detector response, according to the
particle energy and position of incidence. This reposiroty is dedicated to hold
all tuning scripts for each subgroup in the ATLAS e/g trigger group. 

> Do not change anything in the master branch.

> This repository is dedicated to all analysis made by **jodafons** (Github user).

## Introduction:

Proliferation of big data applications is an outcome of the technological
breakthrough during the Digital Era. Rare events of interest immersed in a
large amount of data ensure in a particular scenario where online decision
taking is needed to discard irrelevant information while maintaining
potentially useful events. Offline analysis provides the final decision through
the scrutiny of those events. In such scenarios, the rare incidence of
interesting events does not allow the creation of a bias in the observations by
the online filtering process. At the same time, a high filtering efficiency is
required in order to occupy the output bandwidth only with events potentially
interesting for the offline analysis.

High energy physics experiments were early pioneers of dealing with the big
data applications and their legacy is currently being continued by the
experiments at the Large Hadron Collider (LHC) at CERN, Geneva, Switzerland.
The LHC is the currently leading edge collider, providing high energy
collisions through two opposite way circular beams that allow to study rare
physics processes.  One successful example is the Higgs boson discovery at the
LHC in 2012, only half century after its theoretical prediction, which resulted
in the laureation of P.  Higgs and F. Englert with the Physics Nobel prize.
ATLAS, which is the largest experiment at the LHC, played an important role in
this discovery.

To allow the observation of rare physics processes like the Higgs boson
production, the protons at the LHC are placed along the ring to collide
typically every 25ns, therefore providing high-event input rate (over 30MHz) to
the experiments. It is not viable to record and process all these events due to
the large amount of information generated, i.e. the ATLAS experiment alone
would require a bandwidth of ~70GB/s while the data taking period can expand
for decades. Therefore, online filtering, performed by the ATLAS Trigger and
Data Acquisition System (TDAQ), is required to select interesting events to
reduce the recorded rate to viable levels for storage and further offline
processing.

The trigger system relies on pattern recognition to identify physics objects of
interest to the ATLAS analyses. These objects are filtered in two sequential
levels in order to achieve the low latency driven by the LHC collision rate.
The first level (L1) is based on hardware and has a latency of less than 2.5ms,
while reducing the input rate to, at most, 100kHz.  The second level, called
the High Level Trigger (HLT), has a software-based filtering with a mean target
latency of 550ms and an average output rate of 1kHz.

Each physics object has its own filtering features.  The physics objects
studied here are focused on electron-based channels, which are found in many
interesting physics phenomena, for example the decays of the Higgs boson.
Electron pattern recognition relies on discriminating information of the ATLAS
calorimeter system for energy measurement and its inner tracking Detector for
signal patterns through particle tracks, which involves image processing-like
algorithms. The latter requires higher processing resources, therefore, as a
way to achieve lower latency for electron triggering, early discrimination
evaluates only calorimetry information.

In order to collect more data required for conclusive experimental results on
even rarer physics processes, the LHC has increased the number of collisions.
One way to achieve this, is to squeeze the beam, which results in higher number
of collisions per bunch-crossing (pile-up). This generates higher pressure on
the trigger system, where not only there is more information to be processed,
requiring more bandwidth and processing resources, but also the decision taking
process is harder to perform once signals overlap deteriorating the distinctive
patterns used for particle identification.  This is also the case for electron
identification patterns that are affected by the ever-increasing pile-up at the
LHC.

To account for this effect, the ATLAS experiment upgraded in 2017 the initial
selection performed in the HLT electron filtering to an ensemble of neural
networks algorithm (NeuralRinger). The ensemble is fed only from calorimetry
information contained in concentric rings of energy deposition, which compacts
the information through physics expert knowledge, while keeping the
discriminating patterns.

## Organization:

This repository is dedicated to include all analysis for the ringer group where 
each branch must be assigned to some one. The branches are tagged follow the 
physics channel type name and the LHC periods (for example: channel_period).


- `zee_run2`: This branch is dedicated to all analysis during the Run 2. This branch was assigned to João Victor Pinto and Werner Freund as responbles;


## Notes:
> **INFO**:When a new branch is created, you should update this readme.
> **WARNING**: This is a public repository.


## Contributions:

- João Victor da Fonseca Pinto (jodafons@cern.ch);
- Werner Freund (wsfreund@cern.ch);
- Micael Verissimo (mverissi@cern.ch);
- José Manoel de Seixas (seixas@lps.ufrj.br);

