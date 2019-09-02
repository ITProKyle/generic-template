# generic-template

A generic template for GitHub repos.

## Commands

| Command               | Description                            |
|-----------------------|----------------------------------------|
| `make deploy <env>`   | Execute runway for a given environment |
| `make destroy <env>`  | Execute runway for a given environment |
| `make plan <env>`     | Execute runway for a given environment |
| `make sync`           | Sync python environment with pipfile   |

## Setup

This section outlines how to setup portions of the repo that cannot be reasonably automated.

### Labels

1. Install [git-labelmaker](https://github.com/himynameisdave/git-labelmaker).
   - `npm i -g git-labelmaker`
2. [Generate a GitHub token](https://github.com/settings/tokens) with **repo** permissions.
3. Run `git-labelmaker` to initialize your session using the token.
4. Select the `Add Labels From Package` in the `git-labelmaker` menu and enter `./.github/labels.json`.
