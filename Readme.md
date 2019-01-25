# Math 802 Resources

I'll use this repository to distribute any extra (non-assignment) materials for the class.  In particular, you can find useful configuration files in the ``configuration/`` directory.

Below, you'll find tips on setting up your development environment correctly.  I'll probably update this throughout the semester to address various snags.

## Setup ideas

If you can't (or don't want to) use the recommended setup in the syllabus, here are a few ideas to get you started.

1. You can choose a different IDE.  Spyder, for example, is a more traditional-looking IDE and can be installed easily in Anaconda.
1. You can simplify and simply use a text editor + command prompt.  Some good text editors I use regularly include.
    - Emacs (or Spacemacs)
    - vim
    - Sublime
1. If you need or prefer a purely online option, CoCalc might work well for you.  They have free accounts (though you may want to upgrade for a few dollars per month while enrolled in this class to have more stable access), a huge number of pre-installed Python packages, and stellar technical support.

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

My recommendation is to create a folder (e.g. ``math802s19``) and to clone each assignment repository in there. For example, for the in-class demonstrations, I have cloned the assignment repositories into the folder

``D:\Dropbox\wrk\teaching\MATH802\MATH802S19\demos``

on my computer.  Then I placed ``.pylintrc`` into the demos folder.  So the structure looks something like this (visualized with the help of the ``tree`` command).

    (math802) D:\Dropbox\wrk\teaching\MATH802\MATH802S19\demos>tree
    D:.
    │   .pylintrc
    │
    ├───00-intro-nathan-albin
    │       .gitignore
    │       Readme.md
    │       sparse_tools.py
    │       sparsity_demo.py
    │       test_sparse_tools.py
    │
    ├───01-1d-elliptic-fd-nathan-albin
    │       .gitignore
    │       convergence_demo.py
    │       elliptic_tools.py
    │       fd_tools.py
    │       Readme.md
    │       test_elliptic_tools.py
    │       test_fd_tools.py
    │       timing_demo.py
    │
    └───math-802-course-materials
        │   .gitignore
        │   Readme.md
        │
        ├───configuration
        │       .pylintrc
        │       environment.yml
        │       Readme.md
        │
        └───slides
            └───01-tools-intro
                │   tools-intro.pdf
                │   tools-intro.tex
                │
                └───images
                        folder_post_git.png
                        folder_pre_git.png
                        github.png
                        git_log.png
                        pylint.png
                        pytest.png

Using this structure allows you place ``.pylintrc`` in one place and to run ``pylint`` and ``pytest`` on your projects simply.  You just run them both from the *parent* directory (the ``demo`` directory in my case).  For example, here's how ``pylint`` works for me.

    (math802) D:\Dropbox\wrk\teaching\MATH802\MATH802S19\demos>pylint 00-intro-nathan-albin

    ************* Module sparse_tools
    00-intro-nathan-albin\sparse_tools.py:34:6: W0511: TODO: FIX THIS (fixme)
    00-intro-nathan-albin\sparse_tools.py:35:0: C0303: Trailing whitespace (trailing-whitespace)

    ------------------------------------------------------------------
    Your code has been rated at 9.84/10 (previous run: 9.84/10, +0.00)

Using ``pylint`` this way tells it to check all files in the given directory.

Similarly, to run ``pytest``, I just do this:

    (math802) D:\Dropbox\wrk\teaching\MATH802\MATH802S19\demos>pytest -v --tb=no 00-intro-nathan-albin
    =============================== test session starts ===============================
    platform win32 -- Python 3.7.1, pytest-4.1.0, py-1.7.0, pluggy-0.8.1 -- C:\Users\natha\Anaconda3\envs\math802\python.exe
    cachedir: .pytest_cache
    rootdir: D:\Dropbox\wrk\teaching\MATH802\MATH802S19\demos, inifile:
    collected 7 items

    00-intro-nathan-albin/test_sparse_tools.py::test_5 FAILED                    [ 14%]
    00-intro-nathan-albin/test_sparse_tools.py::test_6 FAILED                    [ 28%]
    00-intro-nathan-albin/test_sparse_tools.py::test_7 FAILED                    [ 42%]
    00-intro-nathan-albin/test_sparse_tools.py::test_bigger[18] FAILED           [ 57%]
    00-intro-nathan-albin/test_sparse_tools.py::test_bigger[21] FAILED           [ 71%]
    00-intro-nathan-albin/test_sparse_tools.py::test_bigger[33] FAILED           [ 85%]
    00-intro-nathan-albin/test_sparse_tools.py::test_bigger[42] FAILED           [100%]

    ============================ 7 failed in 0.38 seconds =============================

If you want to understand the `-v` and `--tb=no` parts, you can read the documentation of ``pytest``, but basically speaking the first one makes it tell me the results of individual tests and the second part keeps it from spitting out a bunch of code showing where the errors occurred.
