#########################
Documentation Style Guide
#########################

Style guides to follow when writing documentation for this project.

.. contents:: Table of Contents
  :local:



**********
Docstrings
**********

In general, this project loosely follows the `Google Python Style Guide for Comments and Docstrings`_.

We use the ``napoleon`` extension for Sphinx to parse docstrings.
Napoleon provides an `Example Google Style Python Docstring`_ that can be referenced.


.. _Example Google Style Python Docstring: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
.. _Google Python Style Guide for Comments and Docstrings: http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings



***************************
reStructuredText Formatting
***************************

In general, this project loosely follows the `Python Style Guide for documentation`_.

.. _Python Style Guide for documentation: https://devguide.python.org/documenting/#style-guide

reStructuredText Whitespace
===========================

All reST files use an indentation of 2 spaces; no tabs are allowed.
There is no maximum line length but 80 characters is the recommended line length for normal text.
It is preferred to only break a line at the end of a sentence.

Code example bodies should use normal indentation based on the convention of the language.

Make generous use of blank lines where applicable; they help group things together.


reStructuredText Sections
=========================

Section headers are created by underlining (and optionally overlining) the section title with a punctuation character, at least as long as the text.

1. ``#`` with overline, for **h1** (generally only one per file, at the top of the file)
2. ``*`` with overline, for **h2**
3. ``=``, for **h3**
4. ``-``, for **h4**
5. ``^``, for **h5**
6. ``"``, for **h6**

**h1** and **h2** should have two or more blank lines separating them from sections with headings of the same level or higher.

A ``rubric`` directive can be used to create a non-indexed heading.

.. rubric:: Example
.. code-block:: rst

  #########
  Heading 1
  #########


  *********
  Heading 2
  *********

  Heading 3
  =========

  Heading 4
  ---------

  Heading 5
  ^^^^^^^^^

  Heading 6
  """""""""

  .. rubric:: Non-indexed Heading


  *********
  Heading 2
  *********

  Heading 3
  =========
