# Memento Migration Data

The CSV file contains information about the migration of mementos from the Library and Archives Canada web archive, described in the blog post and academic publication mentioned below.

CSV file contains the following fields:

* original_URI-M
* final_original_URI-M - *after any redirection*
* final_original_URI-M_status_code
* new_URI-M
* final_new_URI-M - *after any redirection*
* final_new_URI-M_status_code
* delta - *between datetime of original and new*
* same_final_URI-Rs?
* same_final_URI-Ms_status_codes?

Blog post:  
"Where did the archive go? Part 1: Library and Archives Canada", https://ws-dl.blogspot.com/2019/08/2019-08-30-where-did-archive-go-part1.html

Academic Reference:  
Mohamed Aturban, Michael L. Nelson, and Michele C. Weigle, “Where Did the Web Archive Go?,” In Proceedings of the Theory and Practice of Digital Libraries Conference (TPDL). September 2021. Best Research Paper Award. https://arxiv.org/abs/2108.05939

BibTeX:
```bibtex
@INPROCEEDINGS {aturban-tpdl21,
      author = {Mohamed Aturban and Michael L. Nelson and Michele C. Weigle},
      title = {Where Did the Web Archive Go?},
      booktitle = {Proceedings of the Theory and Practice of Digital Libraries Conference (TPDL)},
      year = {2021},
      month = sep,
      arxiv = {https://arxiv.org/abs/2108.05939}
}
```
