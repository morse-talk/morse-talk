from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.md')) as f:
    long_description = f.read()

setup(
	name='morse-talk',
	version='0.1.1',
	author='Himanshu Mishra',
	author_email='himanshu2014iit@gmail.com',
	description='An aide to Morse Code',
	long_description=long_description,
	url='https://github.com/orkohunter/morse-talk',
	download_url='https://github.com/orkohunter/morse-talk/archive/master.zip',
	license='MIT',
	classifiers = [
	'Development Status :: 4 - Beta',
	'Programming Language :: Python :: 2',
	'Programming Language :: Python :: 3',
	],
	keywords='morse code talk',
	packages=[
	'morse_talk'
	]
	)
