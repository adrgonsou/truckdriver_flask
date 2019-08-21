from setuptools import setup, find_packages

setup(
    name='trucker_api',
    version='1.0.0',
    description='Flask API RESTPlus',
    packages=find_packages(),
    install_requires=['flask-restplus==0.9.2', 'Flask-SQLAlchemy==2.1'],
)
