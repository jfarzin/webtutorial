try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'django polling tutorial',
    'author':'Janine Farzin',
    'url': 'https://docs.djangoproject.com/en/3.2/intro/install/',
    'download_url': 'Where to download it',
    'author_email': 'jwaliszewski at gmail'
    'version': '0.1',
    'install_requires': ['pytest'],
    'packages': ['webtutorial'],
    'scripts': [],
    'name': 'Django web tutorial'
}

setup(**config)