# coding: utf-8

"""
    monitoring

    OpenAPI spec version: 2018-06-25T02:38:27Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "ncloud-monitoring"
VERSION = "1.0.5"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="monitoring",
    keywords=["monitoring"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True
)
