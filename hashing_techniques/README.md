# Different techniques for generating fixity information (e.g., hash values) on archived web pages

It is not easy to generate repeatable fixity information or hash values on the playback of archived web pages ([see our technical report: Difficulties of Timestamping Archived Web Pages](https://arxiv.org/abs/1712.03140)). In one of our [studies](https://www.slideshare.net/maturban/it-is-hard-to-compute-fixity-on-archived-web-pages-101663904), we downloaded 17,074 archived web pages, or mementos, 20 times within 5 months. We generated one hash value for each memento after each download. The results show that about 88.45% of mementos produce at least two different hash values. One of the reasons for getting different hash values is that we use multiple components in hash calculation including resources' URIs embedded in an archived page, their HTTP response headers and entity bodies, and the HTTP status codes of these resources. Therefore, any small change (e.g., JavaScript creates URIs with random values) affecting one or more of these components comprising  an archived page will result in different hash values.

In addition to the current hashing technique we use to generate hash values on archived pages, we introduce two additional techniques, URI-M based (or URIs of mementos) and Entity based hashing techniques for generating hash values on archived pages. We want to assess how these two hashing techniques can help produce repeatable hash values.  

# UR-M based hashing technique

In the URI-M based hashing technique we only consider the URI-Ms of resources, comprising an archived page, in hash calculation. Therefore, any changes in HTTP response headers/entities and status codes will not affect final hash values. 
 
# Entity based hashing technique

The entity-based hashing technique considers only the HTTP entity bodies of resources comprising, an archived page, in the hash calculation. It answers the question whether or not an archived page contains the same HTTP entity bodies over time. Thus, this technique concerns about observing the entity bodies of resources regardless of the locations (or URI-Ms) from which these resources are retrieved. We expect this technique to produce more repeatable hash values than other techniques because, in many cases, archival redirects or changes in HTTP response headers will not affect the resulting hash values.

# We always detect new hash values after each download/playback

We compare the three techniques by generating several animated GIF files for each archive of 17 public web archives to show the number of resources requested each time we download the set mementos from the archive. The blue, red, green colors in the animated GIFs (e.g., the three Figures below) indicate that the URI-M based, all components based, and entity-based hashing techniques are used, respectively. 

![alt text](https://github.com/oduwsdl/mementos-fixity/blob/master/hashing_techniques/Maturban_all_resources_over_time_IA_urim_2.gif?raw=true "Resources (URI-Ms) requested in downloads 1 to 39 from the Internet Archive. Blue = URI-M is requested, Gray = URI-M is not requested. Total URI-Ms requested by download 39 is 81,035.")


![alt text](https://github.com/oduwsdl/mementos-fixity/blob/master/hashing_techniques/Maturban_all_resources_over_time_IA_all_2.gif?raw=true "Each point (or resource) = hash(HTTP response headers, HTTP entity body, HTTP status code, URI-M).")

![alt text](https://github.com/oduwsdl/mementos-fixity/blob/master/hashing_techniques/Maturban_all_resources_over_time_IA_entity_2.gif?raw=true "Entities returned in the downloads 1 to 39 from the Internet Archive. Green = Entity is returned, Gray = Entity is not returned.")

The unique resources (or their hashes) are represented by points/dots in the figures and stacked in rows, so each point represents one resource. The location of a resource does not change regardless in all download, but the number of unique resources increases over time (i.e., new resources are requested in each download).  The only special meaning to the position (x, y) of a resource is that resources appear on the bottom of the figures (e.g., download 1) are requested before resources appear at the top (e.g., download 39).

We have several observations from the three figures above and these should apply to most of the animated GIFs available in this repository:
 
* Ideally, the same number of resources should be requested in each download. However, our study indicates that new resources are requested on every download. The Figure below shows the number of new resources requested on each download from archive.org

![alt text](https://github.com/oduwsdl/mementos-fixity/blob/master/hashing_techniques/Maturban_new_resources_per_download_ia_urim.png?raw=true "The number of new resources requested after each download from the Internet archive.")

* The number of requested URI-Ms in Download 1 (baseline download) in the first Figure above is only 40,500 compared to the total number of resources requested by Download 39, which is 81,035 URI-Ms. Download 1 requested only 50% of the total number of resources seen by Download 39.

* The colored area (points with blue, red, or green color) under the baseline download line in all animated GIFs are denser than areas above the baseline download line. This indicates that resources requested in Download 1 have a higher chance of getting requested in the future than new resources requested in downloads 2-39.

* The animated GIFs demonstrate that the entity hashing technique produces fewer new hash values than the other techniques. 

# Summary of the three hashing techniques 
The animated GIF shows how the pool of all seen resources has increased over time and whether a current download requests previously seen resources
- The red GIF: Each resource (point) in the red GIF represents whether the hash value (calculated by Hash(URI-M + Status + Entity + Hdrs)) has been seen (color=red) or not (color=gray)
- The blue GIF: Each resource (point) in the blue GIF represents whether the URI-M of the resource is requested (color=blue) or not (color=gray)
- The green GIF: Each resource (point) in the green GIF represents whether the entity of the resource with "200-OK" has been seen (color=green) or not (color=gray)
