from setuptools import setup, find_packages
import sys

sys.path.insert(0, 'morse_talk')
import release


setup(
    name=release.name,
    version=release.__version__,
    author=release.__author__,
    author_email=release.__email__,
    description=release.__description__,
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
    install_requires=['sounddevice', 'matplotlib'],
    entry_points={
        'console_scripts': [
            'mplot=morse_talk.cli_mplot:main',
            'msound=morse_talk.cli_msound:main',
            'mtree=morse_talk.cli_mtree:main',
            'mgui=morse_talk.gui_func.main',
        ],
    },
    test_suite='nose.collector',
    tests_require=['nose>=0.10.1']

)
