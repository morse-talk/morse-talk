#! /usr/bin/env bash
status_code=$?
function chk()
{ 
    let "status_code=$status_code||$?";
}
if [ "$1" != "nopep8" ] && [ "$2" != "nopep8" ];
    then
    {
        echo "Starting PEP8 Test";
        pep8 --exclude="build/*" --ignore=E501 ./; chk;
        echo "PEP8 Test ended";
    }
else
    echo "PEP8 Test skipped";

fi

cd morse_talk/; chk;
nosetests -v; chk;
nosetests3 -v -v; chk;
nosetests3 -v  --with-coverage --cover-package=morse_talk
exit $status_code;

