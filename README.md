# mementos-fixity

This data set is from the longitudinal study that is the basis of [Mohamed Aturban](https://twitter.com/maturban1)'s PhD disssertation, "[A Framework for Verifying the Fixity of Archived Web Resources](https://ws-dl.blogspot.com/2020/09/2020-09-28-phd-is-very-long-tunnel-with.html)" (Old Dominion University, August 2020).  

Terms:

* URI-R - Uniform Resource Identifier (URI) of the original resource (original webpage)
* URI-M - URI of an archived webpage, or memento, at a given datetime
* TimeMap - provides a list of mementos (URI-Ms) for a given URI-R

[`final_urims.txt`](https://github.com/oduwsdl/mementos-fixity/blob/master/final_urims.txt) is the list of URI-Ms for 16,627 archived web pages, or mementos, of 3,698 unique live webpages from 17 public web archives.

Python scripts that were used in compiling the data set are included in the repo.

The subdirectories, hashing_techniques and memento_migration, contain data from subsequent analysis of mementos in this data set.

The table below shows the number of mementos collected per archive and how they are distributed through time.  The same data is available in [`urims-per-year.csv`](https://github.com/oduwsdl/mementos-fixity/blob/master/urims-per-year.csv).

<pre>
    Archive              URI-Ms 1996  97   98   99 2000   01   02   03   04   05   06   07   08    09    10    11    12    13    14    15    16   17 
----------------------------------------------------------------------------------------------------------------------------------------------------
webarchive.loc.gov       1,594    -    1    1    1    4  100  100  100   99  100  100  100  100    98    99    99    99    98    98    99    98    -
vefsafn.is               1,589    6    8   10   11   11   13   13   14   42   46   74   71   70    85   102   116   140   153   152   152   150  150
webcitation.org          1,585    -    -    -    -    -    -    -    -    -   28   89   85   70   119   156   156   157   156   155   130   127  157
arquivo.pt               1,569   30   14   14   15   15    -    -    -    -    1    1    -  163   167   166   163   162   167   165   164   162    -
web.archive.org          1,566   73   73   73   69   71   71   72   73   72   73   72   72   72    72    70    69    69    67    70    71    72   70
archive.is               1,396   11   10    9   12   10   12   14   13   18   14   20   33   25    29    28    59    12   214   214   214   213  212
wayback.archive-it.org   1,383   17   15    2    1    3    1    1    -    1   51  109  107  108   105   109   107   106   109   107   107   109  108
swap.stanford.edu        1,222    -    -    -    -    -    -    -    -    -    -    -   21   77   185   166   119   135   164   180   140    21   14
nationalarchives.gov.uk    994    -    -    -    -    -    -    1    2   25   12   50   40   97   117   106   110   104    94    83    59    54   40
europarchive.org           979    -    -    -    -    -    -    -    -    -    -    -    -    -     -     -   120   219    72   172   146   213   37
webharvest.gov             712    -    -    -    -    -    -    -    -  128    -  126    -   91     -   129     2   127    59    38    12     -    -
digar.ee                   488    -    -    -    -    -    -    -    -    -    -    -    -    -     -    36    95    69    89    69    74    56    -
proni.gov.uk               469    -    -    -    -    -    -    -    -    -    -    -    -    -     -    17    94    19    75    75    78    59   52
collectionscanada.gc.ca    351    -    -    -    -    -    -    -    -    -   40  173  138    -     -     -     -    -      -     -     -     -    -
webarchive.org.uk          349    -    -    -    -    -    -    -    -    -    6    9   10   31    34    31    34    34    30    34    29    34   33
archive.bibalex.org        199    -    -    1    -    -    -    -    -    -    -    1    -    -     -     -    99    98     -     -     -     -    -
perma-archives.org         182    -    -    -    -    -    -    -    -    -    -    -    -    -     -     -     -     -     -    23    53    53   53
----------------------------------------------------------------------------------------------------------------------------------------------------
Total                           137  121  110  109  114  197  201  202  385  371  824  677  904 1,011 1,215 1,442 1,550 1,547 1,635 1,528 1,421  926
</pre>

To cite this data set, please cite "[Collecting 16K archived web pages from 17 public web archives](https://arxiv.org/abs/1905.03836)":

```
@techreport{aturban:16kpages,
        title = {Collecting {16K} archived web pages from 17 public web archives},
        author = {Mohamed Aturban and Michael L. Nelson and Michele C. Weigle},
        year = {2019},
        number = {arXiv:1905.03836},
}
```
