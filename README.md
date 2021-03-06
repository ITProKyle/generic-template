# generic-template

[![Documentation Status](https://readthedocs.org/projects/generic-template/badge/?version=stable)](https://generic-template.readthedocs.io/en/stable/)

A generic template for GitHub repos.

## Commands

| Command               | Description                            |
|-----------------------|----------------------------------------|
| `make sync`           | Sync python environment with pipfile   |

## Setup

This section outlines how to setup portions of the repo that cannot be reasonably automated.

### Labels

1. Install [git-labelmaker](https://github.com/himynameisdave/git-labelmaker).
   - `npm i -g git-labelmaker`
   - `npm i -g git+ssh://git@github.com:invisiblehats/git-label.git#f067884a399231926c1ae537639ebed6925085ac` is needed until a PR is merged to work with descriptions - <https://github.com/jasonbellamy/git-label/pull/24>
2. [Generate a GitHub token](https://github.com/settings/tokens) with **repo** permissions.
3. Run `git-labelmaker` to initialize your session using the token.
4. Select the `Add Labels From Package` in the `git-labelmaker` menu and enter `./.github/labels.json`.

### Development Environment

1. `export $(cat .env | xargs)` to setup environment variables.
2. `make sync` or `pipenv sync --dev --three` after completing **Step 1**.
