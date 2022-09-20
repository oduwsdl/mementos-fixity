# Different techniques for generating fixity information (e.g., hash values) on archived web pages

It is not easy to generate repeatable fixity information, or hash values, on the playback of archived web pages (see our technical report ["Difficulties of Timestamping Archived Web Pages"](https://arxiv.org/abs/1712.03140) and Mohamed Aturban's dissertation, ["A Framework for Verifying the Fixity of Archived Web Resources"](https://digitalcommons.odu.edu/computerscience_etds/125/)).
We performed a study on the replay of 16,627  archived webpages, or mementos, from 17 public web archives. We replayed and downloaded the mementos 39 times using a headless browser over a period of 442 days and generated a hash for each memento after each download, resulting in 39 hashes per memento.  

We would expect that the hash for the same memento would not change over time. However, our results indicate that 88.45% of the studied mementos produce more than one unique hash value, and about 16% (or one in six) of those mementos always produce different hash values.

## Hashing techniques

In addition to the original hashing technique, which we term as "full hashing", we introduce two additional techniques, URI-M based and entity based hashing. We want to assess how these two hashing techniques can help produce repeatable hash values.  

### Full hashing

We originally used multiple components in hash calculation. For each resource, we include the resource's HTTP entity body, HTTP response status code, URI-M, and selected HTTP response headers (`Memento-Datetime`, `Location`, `Content-Type`, `X-Archive-orig-*`). Therefore, any small change (e.g., JavaScript can create URIs with random values) affecting one or more of these components comprising an archived page will result in different hash values.

### URI-M based hashing

In URI-M based hashing we only consider the URI-Ms of resources comprising an archived page in hash calculation.

### Entity based hashing

The entity-based hashing technique considers only the HTTP entity bodies of resources comprising an archived page in the hash calculation. It answers the question whether or not an archived page contains the same HTTP entity bodies over time. Thus, this technique observes the entity bodies of resources regardless of the locations (or URI-Ms) from which these resources are retrieved. We expect this technique to produce more repeatable hash values than other techniques because, in many cases, archival redirects or changes in HTTP response headers will not affect the resulting hash values.

## Analyzing hash changes per archive

We compare the three techniques by generating animated GIFs files for each of the 17 public web archives to show the number of resources requested each time we download the set of mementos from the archive. The figures show how the pool of observed resources has increased over time and whether a current download requests previously seen resources.

We use color to distinguish between the hashing techniques:

* full (red): Each point in the figure represents whether the resource's hash value (calculated by Hash(URI-M + Status + Entity + Headers)) has been seen (color=red) or not (color=gray)
* URI-M based (blue): Each point in the figure represents whether the URI-M of the resource is requested (color=blue) or not (color=gray)
* entity based (green): Each point in the figure represents whether the entity of the resource with "200-OK" has been seen (color=green) or not (color=gray)

The unique resources (or their hashes) are represented by points/dots in the figures and stacked in rows, so each point represents one resource. The location of a resource does not change regardless in all download, but the number of unique resources increases over time (i.e., new resources are requested in each download).  The only special meaning to the position (x, y) of a resource is that resources appear on the bottom of the figures (e.g., download 1) are requested before resources appear at the top (e.g., download 39).

![alt text](https://github.com/oduwsdl/mementos-fixity/blob/master/hashing_techniques/urim_hashing/Maturban_all_resources_over_time_IA_urim_2.gif?raw=true "Resources (URI-Ms) requested in downloads 1 to 39 from the Internet Archive. Blue = URI-M is requested, Gray = URI-M is not requested. Total URI-Ms requested by download 39 is 81,035.")

![alt text](https://github.com/oduwsdl/mementos-fixity/blob/master/hashing_techniques/full_hashing/Maturban_all_resources_over_time_IA_all_2.gif?raw=true "Each point (or resource) = hash(HTTP response headers, HTTP entity body, HTTP status code, URI-M).")

![alt text](https://github.com/oduwsdl/mementos-fixity/blob/master/hashing_techniques/entity_hashing/Maturban_all_resources_over_time_IA_entity_2.gif?raw=true "Entities returned in the downloads 1 to 39 from the Internet Archive. Green = Entity is returned, Gray = Entity is not returned.")

We have several observations from the three figures above and these should apply to most of the animated GIFs available in this repository:

* Ideally, the same number of resources should be requested in each download. However, our study indicates that new resources are requested on every download. The figure below shows the number of new resources requested on each download from archive.org

![alt text](https://github.com/oduwsdl/mementos-fixity/blob/master/hashing_techniques/urim_hashing/Maturban_new_resources_per_download_ia_urim.png?raw=true "The number of new resources requested after each download from the Internet archive.")

* The number of requested URI-Ms in Download 1 (baseline download) in the first figure above is only 40,500 compared to the total number of resources requested by Download 39, which is 81,035 URI-Ms. Download 1 requested only 50% of the total number of resources seen by Download 39.

* The colored area (points with blue, red, or green color) under the baseline download line in all animated GIFs are denser than areas above the baseline download line. This indicates that resources requested in Download 1 have a higher chance of getting requested in the future than new resources requested in downloads 2-39.

* The animated GIFs demonstrate that the entity hashing technique produces fewer new hash values than the other techniques.
