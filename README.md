# git-circle

`git-circle` is a git extension which provides CLI interaction with
your builds on [CircleCI](https://circleci.com/).

This is currently *very* much a work in progress. You can download it, and use
it, but it's in flux and will change quite a bit in the coming days or weeks.

Stay tuned.

## git-circle General Usage

```
usage: git-circle [-h] [-v] [-np] [-l] [-s] [-ar] [-al] [--limit LIMIT]
                  [--today] [--yesterday] [-d DATE]
                  [command] [param]

positional arguments:
  command               The command to run
  param                 Optional param for commands, see commands list for
                        more information

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Run verbosely
  -np, --no-page        Disable paging
  -l, --list            List the commands available
  -s, --stats           Display useful stats at the end
  -ar, --all-remote     Filter by all remote branches (not all commands
                        support this)
  -al, --all-local      Filter by all local branches (not all commands support
                        this)
  --limit LIMIT         Change the default limit for the underlying CircleCI
                        API call (default 30, max 100)
  --today               Limit responses to just those from today (not all
                        commands support this)
  --yesterday           Limit responses to just those from yesterday (not all
                        commands support this)
  -d DATE, --date DATE  Limit responses to just those from a certain date,
                        format YYYY-MM-DD (not all commands support this)
```

## git-circle Commands

### `list-projects`

This command will list the projects you are following, along with their
branches which have run and the statuses of the most recent builds.

Usage:

```
git circle list-projects [-v] [-np]
```

### `last`

This command will display the results of the last build for your current
branch.

Usage:

```
git circle last [-v] [-np]
```

### `build`

This command will display the results of a given build. If called with a build
number, will use that build. If called without a build number, will use the
last build for your current branch.

Usage:

```
git circle build [build_number] [-v] [-np]
```

### `list-builds`

This command will list the recent builds for a given branch. If called with a
branch name, will find the recent builds for that branch. If called without a
branch name, will use the current branch.

Usage:

```
git circle list-builds [branch_name] [-v] [-np] [-s] [-ar] [-al] [--limit] \
                              [--today] [--yesterday] [--date DATE]
```

The following options have special meanings for `list-builds`:

* `-s`/`--stats` : Will display useful statistics at the end.
* `-ar`/`--all-remote` : Will cycle through all of the branches in the
remote git repo and list the recent builds for each. **WARNING: This could,
potentially, be a lot of branches. Use with caution.**
* `-al`/`--all-local` : Will cycle through all of the branches in the local
git repo and list the recent builds for each. **WARNING: This could,
potentially, be a lot of branches. Use with caution.**
* `--limit` : Change the default limit for the number of recent builds to
obtain from CircleCI. The default is 30, and the maximum is 100.
* `--today` : Limit the recent builds to only those with today's date.
* `--yesterday` : Limit the recent builds to only those with yesterday's date.
* `--date` : Limit the recent builds to only those found on a given date. The
date format is YYYY-MM-DD.

### `artifacts`

This command will display the build artifacts for a given build. If called with
a build number, it will display the artifacts for that build. If called without
a build number, it will display the artifacts for the last build of the current
branch.

The artifacts will be grouped by CircleCI nodes (see
[here](https://circleci.com/docs/setting-up-parallelism)) and will, by default,
display the artifacts as they would be found on the nodes. If called with the
`-v`/`--verbose` option then the full artifact path as well as the artifact
URL will also be displayed.

Usage:

```
git circle artifacts [build_num] [-v] [-np] [-s] [-ar] [-al]
```

The following options have special meanings for `artifacts`:

* `-s`/`--stats` : Will display useful statistics at the end, grouped by
branches.
* `-ar`/`--all-remote` : Will cycle through all of the branches in the remote
git repo and display the artifacts for each. **WARNING: This could,
potentially, be a lot of branches. Use with caution.**
* `-al`/`--all-local` : Will cycle through all of the branches in the local
git repo and display the artifacts for each. **WARNING: This could,
potentially, be a lot of branches. Use with caution.**

