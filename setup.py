import re
from setuptools import setup

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('git-circle').read(),
    re.M
    ).group(1)

setup(
    name='git-circle',
    version=version,
    description='CircleCI git extension',
    long_description=
    "A git extension for interacting with CircleCI.",
    url='https://github.com/criswell/git-circle',
    author='Sam Hart',
    author_email='hartsn@gmail.com',

    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Topic :: Software Development :: Version Control',
        'Topic :: Utilities'
    ],
    keywords='git github development circle circleci',

    install_requires=[
        'requests', 'colorama', 'argparse'
    ],

    scripts=['git-circle']
)
