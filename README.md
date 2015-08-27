# git-circle

`git-circle` is a git extension which provides CLI interaction with
your builds on [CircleCI](https://circleci.com/).

This is currently *very* much a work in progress. You can download it, and use
it, but it's in flux and will change quite a bit in the coming days or weeks.

Stay tuned.

# `git-circle` Commands

## `list-projects`

This command will list the projects you are following, along with their
branches which have run on CircleCI and the statuses of the most recent
builds.

Usage:

```
git circle list-projects [-v] [-np]
```

## `last`

This command will display the results of the last build for your current
branch.

Usage:

```
git circle last [-v] [-np]
```

