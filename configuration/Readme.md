# Configuration tools

This directory contains
- ``.pylintrc``: The pylint settings I'll be using to test your code.
- ``environment.yml``: The conda environment file I'm running on my machine.

I may update these files periodically as the semester progresses, so it would be a good idea to subscribe to changes on GitHub.

## Updating your Anaconda environment

If the ``environment.yml`` file changes, you can update your environment in one of two ways.  First, open the Anaconda prompt and locate the directory where the ``environment.yml`` file is located.  Then choose one of the following.

### Update the environment

In many cases, this is the most efficient.  Just type

	conda env update -f environment.yml

and conda should install any missing packages for your environment.

### Remove and recreate the environment

As an alternative, you can remove the current environment you have and create a fresh one.  This can be done through Anaconda Navigator, or you can run the following commands

    conda env remove -n math802
    conda env create -f environment.yml
  
