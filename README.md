# Random number tests in Python 

Ilja Gerhardt, ilja@quantumlah.org, http://gerhardt.ch. 2011

This implements the NIST random number tests in Python. 

Please install argparse, to have a nice wrapper around everything.
As expected, SciPy and NumPy are needed.

Files in this directory:

* randtest.py - the modules which perform the random tests
* testrandom.py - the wrapper around, for easy interfacing, usage: try --help
* README - this file
* data.pi.bin - 10^6 binary digits of Pi in binary format
* data.pi.txt - 10^6 binary digits of Pi in txt format
* data.pi.sht - 25000 binary digits of Pi in txt format

Unfortunately the tests 10,11,12 are very slow, this is because of the 
tallying of large bitstrings over and over again. I will try to implement
a SWIG version, such that timing is improved.


## 2016-12-29

Port to py3 and push to github. You'll need numpy and scipy.


## Quickstart

cat data.pi.sht | ./testrandom.py --join --test 1 2 3 4 5 6 7 8 9 13 14 15 16 17
