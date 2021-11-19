================
Trip Log Project
================

This space provides a place to ..

#. store trip logs &

#. develope an utility (reverse.py)

----------
reverse.py
----------

This utility accepts a *trip* *log* and returns another log of the
same trip going in the opposite direction.

*Trip* *logs* must be in a specific format.
All lines must either be comment lines (first non white space
character is a '#') or begin with a (real or int) number representing
distance (Km or miles) possibly followed by at least one space and some text.

Any comment lines preceeding the first data line are appended to the
output. All other comment lines are ignored.

See the docstring (of reverse.py) for "Usage."

------------------
Trip Logs Included
------------------
Since confidetiality is not an issue, trip logs are kept under the
**Data** subdirectory and included in the repository. If it was, then
this subdirectory would be excluded from the repo and backed up separately.

==========
Repository
==========

To clone the repository::

    git clone git@github.com:alexKleider/TripLog.git


