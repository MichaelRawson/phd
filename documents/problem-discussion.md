# Problem Discussion

## Project Proposal

The [project proposal](http://www.cs.manchester.ac.uk/study/postgraduate-research/projects/description/?projectid=8160) lays down the following:

 * The project is about applying machine learning techniques to the Vampire theorem prover, and by extension theorem provers in general.
 * The logic used will be first-order logic. (This seems rather under-specified, so I take it to mean "the logic Vampire currently supports" --- though given Ahmed's PhD topic, this might be worth pinning down)
 * Any more I've missed?

As far as I'm aware these are non-binding (?), but are good to use as guidance.

The proposal also suggests three possible fruitful areas, but does not limit the project to these.

 1. Strategy scheduling, as seen in e.g. _MaLeS_.
 2. Proof search control. Turn Vampire's knobs individually (possibly during proof search) in order to point the search in the right direction.
 3. Axiom selection. Select which axioms from an available set are relevant to a given problem.

## Thoughts on Proposed Ideas

Using the proposal ideas as inspiration, I've expanded on them a little as follows:

 * Automatic strategy scheduling could be achieved in Vampire by one of:
  - Extracting features from the input problem and learn a relationship between these and the best strategy to employ.
  - Feed the original input problem into the learning algorithm (how?) and learn a relationship as before, but with automatic feature extraction (does this work?).
  - Use search-time information (such as e.g. number of clauses, average clause size...) to select the _current_ strategy at regular intervals (is switching strategy possible in Vampire?), allowing the use of different strategies to achieve different effects.
 * Controlling proof search. I see this as a more-general version of strategy scheduling: since a "strategy" in Vampire is currently merely a collection of pre-set options (correct?), proof search can be controlled (possibly at run-time) by an artificially-intelligent algorithm.
 * Axiom selection: as Giles suggests, pre-selecting common derived clauses from a given problem could avoid wasted effort in proof search. Possibly these derived clauses could be selected in some way by an intelligent system (more thought needed here). Giles is also correct in that axiom selection by machine learning in itself is already being worked on by more competent people than I, so not a good direction to head down.
