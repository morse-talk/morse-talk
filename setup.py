from setuptools import setup, find_packages


setup(
    name='morse-talk',
    version='0.1.3',
    author='Himanshu Mishra',
    author_email='himanshu2014iit@gmail.com',
    description='An aide to Morse Code',
    url='https://github.com/orkohunter/morse-talk',
        download_url='https://github.com/orkohunter/morse-talk/tarball/v0.1',
        license='MIT',
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
