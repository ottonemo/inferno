import os

from setuptools import setup, find_packages


with open('VERSION', 'r') as f:
    version = f.read().rstrip()

install_requires = [
    'numpy',
    'pandas',
    'scikit-learn>=0.18',
    'scipy',
    'pytorch>=0.1.12',
]

tests_require = [
    'pytest',
    'pytest-cov',
]

docs_require = [
    'Sphinx',
    'sphinx_rtd_theme',
    'numpydoc',
]

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.md')).read()
except IOError:
    README = ''

try:
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except IOError:
    CHANGES = ''

setup(
    name='inferno',
    version=version,
    description='scikit-learn compatible neural network library for pytorch',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    extras_require={
        'testing': tests_require,
        'docs': docs_require,
    },
)
