#! /usr/bin/env bash
status_code=$?
function chk()
{ 
    let "status_code=$status_code||$?";
}

# To make nosetests run under different python environments.
function nt()
{
    python $(which nosetests) $1;
}

pep8 --exclude="build/*" --ignore=E501 ./; chk;

cd morse_talk/tests/;

nt .; chk;
nt test_encoding.py; chk;
nosetests --with-coverage --cover-package=morse_talk

exit $status_code;
