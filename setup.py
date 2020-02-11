#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="xray-python-opentracing",
    version="0.0.1",
    description="AWS X-Ray Python OpenTracing Implementation",
    long_description="",
    author="Jeremy Apthorp <nornagon@nornagon.net>",
    license="",
    install_requires=["basictracer>=2.2,<2.3"],
    tests_require=["pytest", "sphinx", "sphinx-epytext"],
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords=[
        "opentracing",
        "aws",
        "xray",
        "awsxray",
        "traceguide",
        "tracing",
        "microservices",
        "distributed",
    ],
    packages=find_packages(exclude=["docs*", "tests*", "sample*"]),
)
