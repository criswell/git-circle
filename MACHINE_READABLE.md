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
ARTIFACT,<node>,<pretty_path>,<path>,<url>
TOTALS,<branch_name>,<node>,<total_artifacts>
```

* **ARTIFACT** is the unique identifier saying that the following line
contains an artifact.
  * **`<node>`** is the node the artifact can be found in.
  * **`<pretty_path>`** is the path of the artifact using the
  `$CIRCLE_TEST_REPORTS` environmental variable
  * **`<path>`** is the full path of the artifact.
  * **`<url>`** is the URL of the artifact.
* **TOTALS** is the unique identifier saying that the following line contains
artifact totals.
  * **`<branch_name>`** is the name of the branch these artifacts belongs to.
  * **`<node>`** is the node the artifacts can be found on.
  * **`<total_artifacts>`** is the total number of artifacts found on that
  node.

## `build`, `latest`, `list-builds`

Each of the commands which display build information will display with the
following format:

```
BUILD,<branch>,<build_number>,<circle_url>,<status>,<outcome>,<lifecycle>,<vcs_url>,<vcs_revision>,<committer_name>,<committer_email>,<build_time>,<start_time>,<stop_time>
TOTALS,<branch_name>,<outcome>,<total>
SUMMARY_SUCCESSFUL,<total_successful>,<average_duration>
SUMMARY_COMPLETED,<total_completed>,<average_duration>
```

* **BUILD** is the unique identifier saying that the following line contains
build information.
  * **`<branch>`** is the branch this build was for.
  * **`<build_number>`** is the build number.
  * **`<circle_url>`** is the URL for the build.
  * **`<status>`** is the status of the build.
  * **`<outcome>`** is the outcome of the build.
  * **`<lifecycle>`** is the lifecycle of the build.
  * **`<vcs_url>`** is the URL for the git repo.
  * **`<vcs_revision>`** is the hash of the latest commit this build includes.
  * **`<committer_name>`** is the name of the person who made the commit.
  * **`<committer_email>`** is the email of the person who made the commit.
  * **`<build_time>`** is the build time in milliseconds.
  * **`<start_time>`** is the time the build started.
  * **`<stop_time>`** is the time the build ended.
* **TOTALS** is the unique identifier saying that the following line contains
build totals.
  * **`<branch_name>`** is the name of the branch in question.
  * **`<outcome>`** is the outcome this line pertains to.
  * **`<total>`** is the total number of builds in this branch which have the
  listed outcome.
* **SUMMARY_SUCCESSFUL** is the unique identifier saying that the following
line contains a summary of the successful builds.
  * **`<total_successful>`** is the total number of successful builds for
  this query.
  * **`<average_duration>`** is the average duration, in milliseconds, of the
  successful builds in this query.
* **SUMMARY_COMPLETED** is the unique identifier saying that the following
line contains a summary of the completed builds.
  * **`<total_completed>`** is the total number of completed builds for this
  query.
  * **`<average_duration>`** is the average duration, in milliseconds, of the
  completed builds in this query.

