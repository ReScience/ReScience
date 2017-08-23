# The reviewing process

A submission takes the form of a
[Pull Request](https://help.github.com/articles/using-pull-requests/) which is
a mechanism in GitHub to request the integration of some code into a
repository. We use this mechanism as the primary source for the review because
it allows to precisely comment each source and to exchange with the author. If
you're unfamiliar with GitHub, do not hesitate to ask advices and informations
to the editor in charge of editing the submission. You can have a look at what
a full [submission](https://github.com/ReScience/ReScience-submission/pull/3)
looks like. Reviewers unfamiliar with git should have a look at
http://git-lectures.github.io

To review a submission, you'll first have to clone the author's repository onto
your desktop environment and each time an author update the manuscript or code
to get reviewer's comment into account, you'll have to update your local copy
using the `git pull` command.

## Reviewer guidelines

### Successful replications

Most articles in Re**Science** reports th successful replication of the
results (figures, tables, ...) of previously published research work.
A full replication covers all the results of the original work, whereas
a partial replication covers only a subset of the results.

The main criteria for acceptance are

 1. The actual replication of the research. The reviewer must evaluate
    the authors' claims about a successful replication, applying the
    standards of the field.

 2. Reproducibility of the replication. The reviewers must be able
    to run the proposed implementation on their computer, and obtain
    the same results as the authors with the limits of the state of
    of the art of the field.

 3. Clarity of the code and the instructions for running it.
    Uncommented or obfuscated code is as bad as no code at all.

 4. Clarity and completeness of the accompanying article, in which the
    authors should clearly state why they think they have replicated
    the paper (same figures, same graphics, same behavior, etc.) and
    explain any obstacles they have encountered during the replication
    work.

The goal of the review is not to "accept" or "reject" a submission but
to help the authors meet the Re**Science** quality standards. Since
Re**Science** targets replication of already published research, there
is no need to judge the relevance or novelty of the work. Every
replication that meets the criteria listed above is welcome in ReScience.

When evaluating the criteria for acceptance, reviewers need to apply
the standards of their field of research. There are no absolute
criteria for two results/figures being equal, so both the success and
the reproducibility of the replication must be judged according to
the degree of equality that can be achieved given the state of the
art of the field. The clarity of the code and instructions must also
be judged in the light of the conventions of the field. As a general
goal, any competent researcher in the field should understand the
paper and be able to understand and run the code. The use of
software packages that are mainstream in the field is encouraged,
but not strictly required. The less well-known a software package
is, the more explanation authors should provide concerning its
capabilities and use.

### Failed replications

A replication attempt can lead to the finding that the results of the
original paper cannot be reproduced, suggesting a mistake or ommission
in the original work. The failure can concern some or all of the results.
Re**Science** accepts reports on replication failures, but requires a
particularly careful examination by the reviewers. The authors must describe
in detail why they believe that the original work is mistaken, and the
reviewers must be convinced by the reasoning offered by the authors.

Authors who are confronted with replication failure are strongly encouraged
to contact the authors of the original work and try to explore the causes
of the replication failure in collaboration with them. This is, however, not
a requirement for publication in Re**Science**.
