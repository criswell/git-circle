# FAQ

## I've installed it as an individual user, and it doesn't work. Help?

If you've installed with

```
pip install --user git-circle
```

and yet you can't find the executable, be sure that the local Python path is
in your `$PATH` environment variable.

Add something like the following to your `~/.bashrc`, `~/.zshrc`, or init
script for whatever shell you're using:

```
# For Linux
if [ -d "$HOME/.local/bin" ]; then
    export PATH="$PATH:$HOME/.local/bin"
fi

# For Mac OS X
if [ -d "$HOME/Library/Python/2.7/bin" ]; then
    export PATH="$PATH:$HOME/Library/Python/2.7/bin"
fi
```

## I'm getting an error on the `-m` option from a script. Help?

If `git-circle` is working fine when run manually, but you're getting the
following error when run from a script:

```
git-circle: error: unrecognized arguments: -m
```

This likely means that you've been running the script from a virtualenv and
that the virtualenv is not being activated properly in the script.

