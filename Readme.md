# Math 802 Resources

I'll use this repository to distribute any extra (non-assignment) materials for the class.  In particular, you can find useful configuration files in the ``configuration/`` directory.

Below, you'll find tips on setting up your development environment correctly.  I'll probably update this throughout the semester to address various snags.

## Setting up a conda environment

If you're using Anaconda/Miniconda, it's fairly simple to install all the tools you need using ``configuration/environment.yml``.  You can either use Anaconda Navigator to do this, or use the command prompt as described [here](https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file).

## Organizing your files

My recommendation is to create a folder (e.g. ``math802s19/``) and to clone each assignment repository in there.  That way, you can place the ``.pylintrc`` file in the outer folder.  Then, running the command

    pylint <assignment_name>

should work as you would expect.