*******
Testing
*******

Requirements for testing
========================
Morse Talk uses the Python nose testing package.
If you don't already have that package installed, follow
the directions here
http://somethingaboutorange.com/mrl/projects/nose

Testing a source distribution
=============================

You can test the complete package from the unpacked source directory with::

   python setup_egg.py nosetests


Testing an installed package
============================

If you have a file-based (not a Python egg) installation you can
test the installed package with 

>>> import morse_talk
>>> morse_talk.test()

or::

   python -c "import morse_talk; morse_talk.test()"

Testing for developers
======================

You can test any or all of Morse Talk by using the "nosetests"
test runner.  

First make sure the Morse Talk version you want to test
is in your PYTHONPATH (either installed or pointing to your
unpacked source directory).  

Then you can run individual test files with::

   nosetests path/to/file

or all tests found in dir and an directories contained in dir::

   nosetests path/to/dir
