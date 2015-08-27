# git-circle

`git-circle` is a git extension which provides CLI interaction with
your builds on [CircleCI](https://circleci.com/).

This is currently *very* much a work in progress. You can download it, and use
it, but it's in flux and will change quite a bit in the coming days or weeks.

Stay tuned.

## git-circle Commands

### `list-projects`

This command will list the projects you are following, along with their
branches which have run on CircleCI and the statuses of the most recent
builds.

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
git list-builds [branch_name] [-v] [-np] [-s] [-ar] [-al] [--limit] \
                              [--today] [--yesterday] [--date DATE]
```

The following options have special meanings for `list-builds`:

* `-s` | `--stats` : Will display useful statistics at the end.
* `-ar` | `--all-remote` : Will cycle through all of the branches in the
remote git repo and list the recent builds for each. **WARNING: This could,
potentially, be a lot of branches. Use with caution.**
* `-al` | `--all-local` : Will cycle through all of the branches in the local
git repo and list the recent builds for each. **WARNING: This could,
potentially, be a lot of branches. Use with caution.**
* `--limit` : Change the default limit for the number of recent builds to
obtain from CircleCI. The default is 30, and the maximum is 100.
* `--today` : Limit the recent builds to only those with today's date.
* `--yesterday` : Limit the recent builds to only those with yesterday's date.
* `--date` : Limit the recent builds to only those found on a given date. The
date format is YYYY-MM-DD.

