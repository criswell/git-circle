# Using machine readable output

Several `git-circle` commands support formatting their output to make them
more "machine readable", meaning that they can more easily be consumed by other
scripts or tools.

The machine readable output is CSV, with each line having a different format
depending upon what command was used.

The first element of each line will *always* be a unique identifier for the
type of data that follows.

Specific formatting for those commands that support machine readable output
is as follows:

## `artifacts`

Each line containing an artifact will have the following format:

```
ARTIFACTS,<node>,<pretty_path>,<path>,<url>
TOTALS,<branch_name>,<node>,<total_artifacts>
```

* **ARTIFACTS** is the unique indentifier saying that the following line
contains an artifact.
  * **<node>** is the node the artifact can be found in.
  * **<pretty_path>** is the path of the artifact using the
  `$CIRCLE_TEST_REPORTS` environmental variable
  * **<path>** is the full path of the artifact.
  * **<url>** is the URL of the artifact.
* **TOTALS** is the unique identifier saying that the following line contains
artifact totals.
  * **<branch_name>** is the name of the branch this artifact belongs to.
  * **<node>** is the node the artifacts can be found on.
  * **total_artifacts>** is the total number of artifacts found on that node.

