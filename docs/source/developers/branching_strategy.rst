##################
Branching Strategy
##################

.. contents:: Table of Contents
  :local:



*************
Master Branch
*************

The **default branch** of this project is ``master``.

This branch can also be thought of as the *latest* branch in that it contains all the latest changes.
It can also be through of as the *development* branch in that it should be an exact match for what is currently deployed to a development and/or test environment where applicable.
All branches should be based off of this branch and should be merged into this branch when a PR has been approved.

The contents of this branch should be continuously deployed to a development and/or test environment where applicable.

Releases are created from this branch by creating a tag.
The tag should be in the format ``v${MAJOR}.${MINOR}.${PATH}`` following SemVer_.
The tagged release should be deployed to a production environment where applicable.

.. _SemVer: https://semver.org/

..
  For a project primarily containing IaC that is not *versioned* or *released*, environment branches should be used in place of the master branch.
  The branches below are provided as an example. More can be added as needs (e.g. staging).

  **************
  ENV-dev Branch
  **************

  This branch can also be thought of as the *latest* branch in that it contains all the latest changes.
  All branches should be based off of this branch and should be merged into this branch when a PR has been approved.

  The contents of this branch should be continuously deployed to a development environment and should represent the state of the development environment at all times.

  ***************
  ENV-test Branch
  ***************

  When a change has completed development and is ready for testing, a PR should be opened from the `ENV-dev Branch`_ to this branch to promote the changes.
  The PR **must** be merged using fast-forward only (``--ff-only``).

  The contents of this branch should be continuously deployed to a test environment and should represent the state of the test environment at all times.

  ****************
  ENV-prod Branch
  ***************

  When a change has been fully tested and is certified as production ready, a PR should be opened from the `ENV-test Branch`_ to this branch to promote the changes.
  The PR **must** be merged using fast-forward only (``--ff-only``).

  The contents of this branch should be continuously deployed to a production environment and should represent the state of the production environment at all times.



****************
Feature Branches
****************

A **feature branch** is a branch where one or more developers are actively developing a single *change*.
This change can be a new feature/functionality, bug fix/patch, documentation update, or maintenance task.

A feature branch must be based off of the `Master Branch`_ and must be merged into the `Master Branch`_ when complete.
Changes to the `Master Branch`_ should be integrated daily.

A feature branch can be deployed to a development environment where applicable.


Feature Branch Naming
=====================

When creating a feature branch, it must be named in a specific way for GitHub Actions to handle it correctly.
The naming format is ``${PREFIX}/${DESCRIPTION_OF_CHANGE}``.

.. rubric:: Prefixes

:bugfix | fix | hotfix:
  The branch contains a fix for a big.

:feature | feat:
  The branch contains a new feature or enhancement to an existing feature.

:docs | documentation:
  The branch only contains updates to documentation.

:chore | maintain | maint | maintenance:
  The branch does not contain changes to the project itself to is aimed at maintaining the repo, CI/CD, or testing infrastructure. (e.g. README, GitHub action, integration test infrastructure)

:release:
  Reserved for maintainers to prepare for the release of a new version.
