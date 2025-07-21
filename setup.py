from setuptools import setup, find_packages

setup(
    name="tutor-pharmacalogica",
    version="0.1.0",
    description="Custom Open edX theme plugin for NeuroPharm Academy",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "tutor.plugin.v0": [
            "pharmacalogica = tutorpharmacalogica"
        ]
    },
)
