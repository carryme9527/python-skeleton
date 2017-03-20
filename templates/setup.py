try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': '$PROJ_DESC',
    'author': '$AUTHOR_NAME',
    'url': '$PROJ_URL',
    'download_url': '$PROJ_DOWNLOAD',
    'author_email': '$AUTHOR_EMAIL',
    'version': '0.0.1',
    'install_requires': ['nose'],
    'packages': ['$PROJ_NAME'],
    'scripts': [],
    'name': '$PROJ_NAME'
}

setup(**config)
