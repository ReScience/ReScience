# Overview of the submission process

The Re**Science** editorial board unites scientists who are committed to the
open source community. They are experienced developers who are
familiar with the GitHub ecosystem. Each editorial board member is specialised
in a specific domain of science and is proficient in several programming
languages and/or environments. Our aim is to provide all authors with an
efficient, constructive and public editorial process.

Submitted entries are first considered by a member of the editorial board, who
may decide to reject the submission (mainly because it has already been
replicated and is publicly available), or assign it to two reviewers for
further review and tests. The reviewers evaluate the code and the accompanying
material in continuous interaction with the authors through the PR discussion
section. If both reviewers managed to run the code and obtain the same results
as the ones advertised in the accompanying material, the submission is
accepted. If any of the two reviewers cannot replicate the results before the
deadline, the submission is rejected and authors are encouraged to resubmit an
improved version later.

## Criteria for Publication

To be considered for publication in Re**Science**, any given submission must
satisfy the following criteria:

* Replicability
* Rigorous methodology
* Original source code
* Substantial evidence for replication of the original results

Furthermore, you cannot submit the replication of your own research, nor the
research of your close collaborators. We believe such restrictions will favor
the cross-fertilization of research and the spread of knowledge.


## Open Access

Re**Science** applies the Creative Commons Attribution (CC BY) license to all
works we publish. Under the CC BY license, authors retain ownership of the
copyright for their article, but authors allow anyone to download, reuse,
reprint, modify, distribute, and/or copy articles in Re**Science** journal, so
long as the original authors and source are cited. No permission is required
from the authors or the publishers.



## How to submit ?

* Create a [GitHub](https://github.com) account
* [Fork](https://github.com/ReScience/ReScience-submission/fork) the
  [ReScience submission](https://github.com/ReScience/ReScience-submission)
  repository
* Clone this new repository into your desktop environment

  ```
  $ git clone https://github.com/YOUR-USERNAME/ReScience-submission
  ```
* Create a branch (the branch name should be author names separated with dashes)

  ```
  $ git checkout -b AUTHOR1-AUTHOR2-...-AUTHORN-YEAR
  ```
* Add your code & article and commit your changes:

  ```
  $ git commit -a -m "Some comment"
  ```
* [Push](https://help.github.com/articles/pushing-to-a-remote/) to GitHub

  ```
  $ git push origin AUTHOR1-AUTHOR2-...-AUTHORN-YEAR
  ```
* Issue a
  [pull request](https://help.github.com/articles/using-pull-requests/) (PR)
  to Re**Science** with title "Review Request" and insert the following text
  in the description:

  ```
  **AUTHOR**

  Dear @ReScience/editors,

  I request a review for the replication of the following paper:

  * References of the paper holding results you're replicating

  I believed the original results have been faithfully replicated
  as explained in the accompanying [article](link to your pdf).
  ```
* Assign the PR to an editor from the
  [editorial board](https://github.com/ReScience/ReScience/wiki/Editorial-Board)
* Answer questions and requests made in the PR conversation page.

You can have a look at a [previous submission](https://github.com/ReScience/ReScience-submission/pull/3)


## Preparation of the material

The structure of a submission is:

~~~
+ README.md
+ article
|  | article.md
|  | article.bib
|  | LICENSE.md (CC-BY 4.0)
|  | ...
|  + ...
+ code
|  | README.md
   | LICENSE.md (to be chosen)
|  | ...
|  + ...
+ data
|  | README.md
|  | LICENSE.md (CC 0)
|  | ...
|  + ...
+ notebook
   | README.md
   | LICENSE.md (to be chosen)
   |
   + ...
~~~

* A top `README.md` file that will be displayed when a reader enters your submission directory (once published)
* An `article.md` file that introduces the original paper, explains the technical details of the replication and gives the evidence for the replication of the original results.
* A `code` directory that contains the **commented** code for the replication.
* A `data` directory that contains any data necessary to run the code.
* A `notebook` directory that may contain notebooks if relevant.
* Don't forget to choose a license for the code repository. You're free
  to choose whatever open license you prefer (see
  [the Debian Free Software Guidelines](https://www.debian.org/social_contract#guidelines))
  but you need to choose one.
