from setuptools import setup

setup(
    name='pynliner',
    version='0.4.0',
    description='Python CSS-to-inline-styles conversion tool for HTML using BeautifulSoup and cssutils',
    author='Tanner Netterville',
    author_email='tannern@gmail.com',
    packages=('pynliner',),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'BeautifulSoup<4.0',
        'cssutils>=0.9.7',
    ],
    entry_points={
        'console_scripts': [
            'pynliner=pynliner:main',
        ]
    }
)
