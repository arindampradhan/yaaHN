try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
setup(
    name='yaaHN',
    version='0.1.1',
    description='Yet another API wrapper for offical Hacker News',
    long_description=open('README.md').read(),
    package_data={'': ['LICENSE.md']},
    url='https://github.com/arindampradhan/yaaHN',
    download_url='https://github.com/arindampradhan/yaaHN/tarball/v0.1',
    author='Arindam Pradhan',
    test_suite='tests',
    license='MIT',

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords=['api', 'hacker news', 'news', 'stories'],
    packages=find_packages(),
    install_requires=['requests==2.5.3', 'grequests'],
    data_files=[],
    entry_points={},
)
print find_packages()
print "\n" * 10
