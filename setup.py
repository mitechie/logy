# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

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
    
setup(
    name='logy',
    version=version,
    description='A flask based web application for central logging',
    author='Victor Lin',
    author_email='bornstub@gmail.com',
    url='https://victorlin@bitbucket.org/victorlin/logy',
    license='MIT',
    packages=['logy'],
    install_requires=[
        'Flask',
        'Flask-Genshi'
    ],
    **extra
)
