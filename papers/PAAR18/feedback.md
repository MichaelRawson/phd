# Reviewer 1
## 2.1

> the strategy/portfolio selection could be done only after the preprocessing and clausification - this is traditionally the way it's done in E

> also, the "preprocessing" strategies can be extremely important, in particular for large theories. See e.g. the E.T system [1] where this is the main work done on top of E.

Yes - exactly the point I think is made?

## 2.2

> there is no mention of AVATAR here - I would expect that it's quite frequently used today in Vampire

Not entirely sure how AVATAR would interact would the strategy priority system. Probably not positively, if I'm honest.

## 3.1

> "real-valued function f(n)" is formally correct, but quite confusing; I'd perhaps use f_n if you think you really need the "n" here, otherwise it looks like f is a nat-valued function

"n" for node, not "n" for natural. But fine, f_n it is.

> the formula defining f(n) looks quite nonstandard: why is A(i) inside?

Oops. Really bad typo. But there is no standard formulation, and I think the one presented is fine once I fix the typo.

## 4

> it's not clear to me how the 10 buckets that produce "fixed trace size" are created

I still haven't come up with a good name for this.
And while the algorithmic process is straightforward, it seems stupid to put that in the paper.
Thoughts?

> in Fig. 4, the Y-axis seems to go from 0 to 5 to 0; I'd rather think it goes from 0 to 10?

It doesn't. I can add a label for "10" if that would help.

> at least some examples of selected features and selected execution traces and their pre/postprocessing into the learning data would probably help a lot - there is enough space allowed for the paper

Possibly, but which features? Could add a graph of an example problem trace I guess.

## 5

> it would be useful to use the ML toolkits to see what are the most discriminating (predictive) features

I agree, but there's no obvious way to do that for a neural network. This isn't a decision tree.

> I would also like to see a comparison with the static features used currently

If I could understand how the static features work.

> also, consider looking at using the feature vector of dynamic proof completion ratios as done in [[3]](https://arxiv.org/abs/1802.04007)

From a quick skim this seems unrelated. I don't think we have a concept of "related proof" yet in Vampire, do we?

## 8

> the ATP evaluation is done on the same data (full TPTP) that was used for training. This is a serious crime in ML - it's much preferable to split the data into a training and testing set.

Not having a train/test split is indeed a cardinal sin in the ML world.
However, we already do the big brother of this (x-validation) to evaluate the ML techniques.
Running Vampire on TPTP having trained on (a subset of) TPTP does seem like cheating, but multiple theorem provers overfit to TPTP anyway.

> I am also wondering how the training data were obtained: if you are just running the CASC mode, then you are not running each strategy for the same time. So already the training data you have would be quite biased.

Yes. But we also rely on CASC-mode to give us a preliminary schedule and maximum TTL for strategies anyway, so it wouldn't make sense to _not_ train with CASC-mode.

> in general, Vampire has been tuned for two decades on TPTP, so it's not surprising that its current CASC mode is hard to beat; consider evaluating the learning/non-learning modes on some less frequented benchmarks - e.g. coming from the ITP libraries (HOL, Mizar, Isabelle)

Tell me about it.
Entirely possible, but probably not for this paper?

# Reviewer 2

> It should be mentioned in the introduction that the paper is mainly focused on how the new approach impacts Vampire and depends on its features

It's in the abstract. But I'm not opposed to it being in the introduction as well.

> In section 4 it would be good to give examples of non-numerical and derivative data to be extracted from Vampire's proof search

I think this was always entirely hypothetical. But you could in principle. Maybe make the hypothetical more obvious?

> page 2: provide a reference for /saturation algorithms with redundancy elimination/

Yes please. Otherwise I can dig around.

> page 3: when mentioning that Vampire includes experimental parameters, clarify what that means and if it has any impact on your approach (I think it's best to just omit this detail)

Yes please - I'm not sure myself.

> page 5: cite the mentioned new work that has started to use deep-neural-network methods

This is the Loos paper mostly. I'll add the citation, it's already in the bibliography and cited above.

# Reviewer 3

> The paper presents a machine learning approach to schedule solving strategies
> in the theorem prover Vampire. The main goal appears to reduce the average 
> runtime, potentially at the cost of solver a few instances less. The presented 
> approach achieves that goal. However, it is also stated that the development of
> Vampire focussed on solving as many instances as possible. So the question
> arises **how well Vampire would perform without the machine learning techniques**
> if the strategies are optimized to lowering the average runtime.

A good question. We should discuss this.

> What seems to be missing is a description of features that were considered important/unimportant by the machine learning approach. Any interesting  insights that can be extracted from this work?

See above.
