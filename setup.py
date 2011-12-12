# -*- coding:utf-8 -*-
import os
from setuptools import setup, find_packages

version = '20111209.01'

setup(
    name='sc.templer.policy',
    version=version,
    description="Template for Portal Policy in Plone projects.",
    long_description=open("README.rst").read() + "\n" +
                     open(os.path.join("docs", "HISTORY.txt")).read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Framework :: Plone",
        "Framework :: Plone",
        "Framework :: Buildout",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='simples_consultoria web plone command-line skeleton project',
    author='Simples Consultoria',
    author_email='products@simplesconsultoria.com.br',
    url='http://www.simplesconsultoria.com.br/',
    namespace_packages=['sc', 'sc.templer'],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
        "sc.templer.core",
        "templer.zope",        
    ],
    entry_points="""
    [paste.paster_create_template]
    portal_policy = sc.templer.policy.template:PortalPolicy
    
    [templer.templer_structure]
    gs_nested_policy = sc.templer.policy.structures:GSPolicyProfileStructure
    """,
    )
