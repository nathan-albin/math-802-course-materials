# Math 802 Resources

I'll use this repository to distribute any extra (non-assignment) materials for the class.  In particular, you can find useful configuration files in the ``configuration/`` directory.

Below, you'll find tips on setting up your development environment correctly.  I'll probably update this throughout the semester to address various snags.

## Helpful links

Here is a collection of documentation/tutorials that might come in handy.

- Python
    - [Official documentation](https://docs.python.org/3/)
    - [Official tutorial](https://docs.python.org/3/tutorial/index.html)
- Numpy
    - [Official documentation](https://docs.scipy.org/doc/numpy/)
    - [Numpy for Matlab Users](https://docs.scipy.org/doc/numpy-1.15.0/user/numpy-for-matlab-users.html)
- [GitHub Guides](https://guides.github.com/)
    - [Git Handbook](https://guides.github.com/introduction/git-handbook/)
    - [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
    - [Video Guides](https://www.youtube.com/githubguides)

## Setting up a conda environment

If you're using Anaconda/Miniconda, it's fairly simple to install all the tools you need using ``configuration/environment.yml``.  You can either use Anaconda Navigator to do this, or use the command prompt as described [here](https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file).

## Organizing your files

My recommendation is to create a folder (e.g. ``math802s19/``) and to clone each assignment repository in there.  That way, you can place the ``.pylintrc`` file in the outer folder.  Then, running the commands

    pylint 00-demo-assignment

or

    pytest -v 00-demo-assignment

should work as you would expect.