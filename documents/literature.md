# Literature

Overview of literature I found useful.
Will use in my literature review later.

## ML+AR Papers

### Parameter Selection

- [Machine Learning and Automated Theorem Proving](http://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-792.pdf) - James P. Bridge's PhD thesis, kind of what I'm aiming for, but with more of a Bayesian twist.
- [_MaLeS_: A Framework for Automatic Tuning of Automated Theorem Provers](https://link.springer.com/content/pdf/10.1007%2Fs10817-015-9329-1.pdf) - automatic strategy selection, and how to identify strategies. Still appears to be Bayesian.
- [Automated Invention of Strategies and Term Orderings for Vampire](http://arxiv.org/pdf/) - add term orderings into the mix for the possible strategy space. Accepted to GCAI 2017.

### Axiom/Premise Selection

- [Deep Network Guided Proof Search](https://arxiv.org/pdf/1701.06972.pdf) - runing a deep neural network in E to select processed clauses.
- [Deep Sequence Models for Premise Selection](https://arxiv.org/pdf/1606.04442.pdf) - selecting premises from the Mizar corpus with deep recurrent/convolutional nets.
- [Learning-Assisted Automated Reasoning with Flyspeck](https://link.springer.com/content/pdf/10.1007/s10817-014-9303-3.pdf) - actually largely about HOL->FOL translation and premise-selection, here to avoid reading it again due to the slightly-misleading title.
- [MaSh: Machine Learning for Sledgehammer](https://people.mpi-inf.mpg.de/~jblanche/mash.pdf) - premise selection for Sledgehammer

### Other

- [Monte-Carlo Tableaux Proof Search](http://cl-informatik.uibk.ac.at/users/cek/docs/17/mfckju-cade17.pdf) - describes implementing MCTS (as used in e.g. _AlphaGo_) in the context of LeanCOP, a tableaux prover.
- [Proof output and machine learning for inductive theorem provers](http://publications.lib.chalmers.se/records/fulltext/238593/238593.pdf) - application of ML in HipSpec, an inductive theorem prover (only part of this is relevant)
- [Efficient Semantic Features for Automated Reasoning over Large Theories](https://www.ijcai.org/Proceedings/15/Papers/435.pdf) - feature selection
- [Breeding Theorem Proving Heuristics with Genetic Algorithms](https://easychair.org/publications/paper/245316) - using GAs intead of ML but targetting the parameter selection problem

## AR papers

- [Proof Search in the Sequent Calculus for First-Order Logic with Equality](https://www.uni-kassel.de/eecs/fileadmin/datas/fb16/Fachgebiete/FMV/Abschlussarbeiten/Masterarbeit_Arno_Ehle.pdf) - Arno Ehle's MSc thesis, not research-level but useful as implementation guide for sequent calculus.
- [First-Order Theorem Proving and VAMPIRE](http://www.cse.chalmers.se/~laurako/pub/CAV13_Kovacs.pdf) - a reasonable overview of Vampire
- [Set of Support for Theory Reasoning](https://easychair.org/publications/paper/346431) - a new method for dealing with theory axioms in Vampire 

## ML Papers??

# Overview, Comparison of Bridge, Other Authors.
Overall, Bridge's thesis is quite simplistic (not a criticism), especially from a machine learning point of view. He attempts two main areas:
- The preliminary experiment attempts to classify provable/unprovable problems.
- Subsequent experiments focus on training a classifier to perform heuristic selection.

Both experiments' methodology involves training a support-vector machine on a hand-engineered set of features, though Bridge's reasons for choosing this arrangement in advance seem minimally-argued and he does not attempt to evaluate other methods later in his thesis.
Perhaps unsurprisingly, the initial experiment does not seem to go well. I'd be very surprised if first-order logic happened to be classifiable by means of an SVM...
Bridge does however produce (seemingly statistically valid) significant results with his method on heuristic selection, which is encouraging for my PhD.

Other authors have more-recently published more-promising papers which appear to supersede Bridge's thesis, notably Urban and Kaliszyk.
Urban in particular has produced work in the space of strategy-selection and proof guidance, with a variety of methods, including more recently "deep learning".
Bridge is more likely useful as an overview and initial experiments, whereas Urban and Kaliszyk's recent work is the state of the art.
