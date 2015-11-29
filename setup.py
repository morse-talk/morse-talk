from setuptools import setup, find_packages
import sys

sys.path.insert(0, 'morse_talk')
import release


setup(
    name=release.name,
    version=release.__version__,
    author=release.author,
    author_email=release.author_email,
    description=release.description,
    url='https://github.com/morse-talk/morse-talk',
    download_url='https://github.com/morse-talk/morse-talk/archive/master.zip',
    license='GPLv2',
    classifiers=[
            'Development Status :: 4 - Beta',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3',
    ],
    keywords='morse code talk',
    packages=[
        'morse_talk'
    ],
    test_suite='nose.collector',
    tests_require=['nose>=0.10.1']

)
