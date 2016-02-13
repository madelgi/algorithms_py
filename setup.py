try:
    from setuptools import setup
except ImportError:
    from docutils.core import setup

config = {
    'description': 'Implementations of popular algorithms and data structures',
    'author': 'Max Del Giudice',
    'url': 'TODO',
    'author_email': 'maxdelgiudice@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': [
        'algorithms_py.utils',
        'algorithms_py.algorithms',
        'algorithms_py.data_structures',
        'algorithms_py.data_structures.hashes',
    ],
    #'test_suite': 'algorithms_py/test',
    'scripts': [],
    'name': 'algorithms_py'
}

setup(**config)
