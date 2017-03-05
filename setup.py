try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A prototyping circuit simulator',
    'author': 'A. Gokcen Mahmutoglu',
    'url': 'https://github.com/gmahmutoglu/csimpy',
    'download_url': 'Where to download it.',
    'author_email': 'amahmutoglu@berkeley.edu',
    'version': '0.1',
    'install_requires': ['nose', 'coverage'],
    'packages': ['csimpy'],
    'scripts': [],
    'name': 'csimpy'
}

setup(**config)
