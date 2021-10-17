###############
Getting Started
###############

Before getting started, `fork this repo`_ and `clone your fork`_.

.. _fork this repo: https://help.github.com/en/github/getting-started-with-github/fork-a-repo
.. _clone your fork: https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository

..
  The fork & clone strategy is primarily for open source projects.
  Private projects should generally be cloned directly as long as you have write access.

.. contents:: Table of Contents
  :local:



*****************************
Local Development Environment
*****************************

Setting up a workstation of development of this project.


Prerequisites
=============

Some of the listed prerequisites are *recommended* but not required.

- `Make (GNU recommended) <https://www.gnu.org/software/make/>`__ for simplified actions

  - ``brew install make`` on macOS
  - ``sudo apt install make`` or ``sudo apt install build-essential`` or Ubuntu/Debian
  - ``winget install -e --id GnuWin32.Make`` on Windows

- `npm <https://docs.npmjs.com/downloading-and-installing-node-js-and-npm>`__ for type checking & spell check (recommended to use nvm to install)
- `poetry <https://python-poetry.org/>`__ for Python virtual environments
- *(recommended)* `direnv <https://direnv.net/>`__ for setting environment variables (POSIX only)
- *(recommended)* `nvm <https://github.com/nvm-sh/nvm>`__ to install and manage different versions of node (POSIX only)

  - see `nvm-windows <https://github.com/coreybutler/nvm-windows>`__ for Windows support

- *(recommended)* `pyenv <https://github.com/pyenv/pyenv>`__ to install and manage different versions of Python (POSIX Only)

  - see `pyenv-win <https://github.com/pyenv-win/pyenv-win>`__ for Windows support

- *(recommended)* `Visual Studio Code <https://code.visualstudio.com/>`__ for standardized IDE settings


Setup
=====

1. Clone the repo or your fork of this repo.
2. Change directory into the cloned directory.
3. Run ``make setup``.
4. Start developing.

By running ``make setup``, the following will happen:

#. poetry is used to setup a Python virtual environment.
#. `pre-commit <https://pre-commit.com/>`__  is configured from the virtual environment to run basic checks and formatting when a commit is made.
   These checks can be run manually using ``make run-pre-commit``.
#. node dependencies are installed.
