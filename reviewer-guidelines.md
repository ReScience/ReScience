# The review process

A submission takes the form of a
[Pull Request](https://help.github.com/articles/using-pull-requests/) which is
a mechanism in GitHub to request the integration of some code into a
repository. We use this mechanism as the primary source for the review because
it allows to precisely comment each source and to exchange with the author. If
you're unfamiliar with GitHub, do not hesitate to ask advices and informations
to the editor in charge of editing the submission. You can have a look at what
a full [submission](https://github.com/ReScience/ReScience-submission/pull/3)
looks like.

To review a submission, you'll first have to clone the author's repository onto
your desktop environment and each time an author update the manuscript or code
to get reviewer's comment into account, you'll have to update your local copy
using the `git pull` command.


## Reviewer guidelines

The main criterion for acceptance is the actual replication of the research
with a clear statement by the authors explaining why they think they have
replicated the paper (same figures, same graphics, same behavior,
etc.). However, keep in mind that the clarity of the code is an important
criterion. Uncommented or obfuscated code is as bad as no code at all. A code
without the accompanying article is also a criterion for rejection since we're
not human compilers (well not all of us at least). The role of the reviewer is
thus to ensure the proposed submission is actually replicable. This means:

1. You should be able to run the proposed implementation on your computer
2. You should obtain the same results as indicated in the accompanying paper
3. These results must correspond to the original paper

The goal of the review is to help the author to meet Re**Science** quality
standards. More specifically, since Re**Science** targets replication of
original research, there is no need to judge the relevance or novelty of the
research. The review should really concentrate on how easy it would be for
another researcher to run the proposed implementation. This should be viewed in
light of the standards in the field. If a given tool/library/software is
mainstream in your field, it is ok to use them, but if a brand new standalone
implementation is proposed, you must not reject it on this criterion.


Reviewers unfamiliar with git should have a look at http://git-lectures.github.io


