from setuptools import setup, find_packages


# --== START SETTINGS ==--

VERSION = '3.0.0'
DESCRIPTION = """
Forked from Morteza Rezaalipour https://github.com/MortezaRezaalipour/z3log.

This fork contains specific changes to be used in https://github.com/LP-RG/subxpat.
"""
REQUIREMENTS_FILE = 'prod.requirements.txt'

# --== END SETTINGS ==--


with open(REQUIREMENTS_FILE, 'r') as ifile:
    requirements = ifile.read().splitlines()

setup(
    name='z3log-xpatvariant',
    version=VERSION,
    author='Morteza Rezaalipour (MorellRAP)',
    author_email='rezaalipour.usi@gmail.com',
    maintainer='Research group of Laura Pozzi',
    url='https://github.com/LP-RG/z3log',
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=requirements,
    keywords=['python', 'verilog', 'circuits', 'synthesis'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: Unix',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
    ]
)
