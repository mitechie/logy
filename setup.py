# -*- coding: utf-8 -*-
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

try:
    from logy import version
    version = version.__version__
except ImportError:
    version = 'unknown'
    
extra = {}
try:
    from logy import scripts
    extra['cmdclass'] = {
        'initdb': scripts.InitdbCommand,
        'serve': scripts.ServeCommand
    }
except ImportError:
    pass

try:
    file = open('README.rst', 'rt')
    content = file.read()
    file.close()
    extra['long_description'] = content
except IOError:
    pass
    
setup(
    name='logy',
    version=version,
    description='A flask based web application for central logging',
    author='Victor Lin',
    author_email='bornstub@gmail.com',
    url='http://bitbucket.org/victorlin/logy',
    license='MIT',
    packages=find_packages(),
    package_data={
        'logy': [
            'templates/*',
            'static/*/*'
        ]
    },
    install_requires=[
        'distribute',
        'Flask',
        'Flask-Genshi',
        'SQLAlchemy',
    ],
    entry_points = {
        'console_scripts': [
            'logy_initdb = logy.scripts:initdb', 
            'logy_run = logy.scripts:run_logy',
        ]
    },
    **extra
)
