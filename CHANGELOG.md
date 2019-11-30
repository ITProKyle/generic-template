# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.0] - 2019-11-30

### Changed

- moved pipenv virtual environment into the project with the `make sync` command and exportable `.env` file
- `.env` is not tracked in the repo
- updated runway pin to `~=1.2`
- ran `pipenv update --dev` to update all packages

### Fixed

- Makefile directives

## [0.2.0] - 2019-09-02

### Added

- label.json file for configuring repo labels using `git-labelmaker`
- issue and pull request templates

## [0.1.0] - 2019-09-01

- initial release of module
