try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='$PROJ_NAME',
    version='0.0.1',
    url='$PROJ_URL',
    license='BSD',
    author='$AUTHOR_NAME',
    author_email='$AUTHOR_EMAIL',
    description='$PROJ_DESC',
    packages=['$PROJ_NAME'],
)
