#! /usr/bin/env python


from setuptools import setup


setup(
    name='markdown_rewritelink',
    version='1.02.1',
    author='Martin Ortbauer',
    author_email='mortbauer@gmail.com',
    description='Python-Markdown extension to have custom callbacks on links)',
    url='https://github.com/mortbauer/markdown_rewritelink/',
    py_modules=['markdown_rewritelink'],
    install_requires=['Markdown>=2.0',],
    classifiers=[
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)
