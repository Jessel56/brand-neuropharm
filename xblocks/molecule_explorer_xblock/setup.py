from setuptools import setup, find_packages
setup(
    name='molecule_explorer_xblock',
    version='1.0.0',
    packages=find_packages(),
    install_requires=['XBlock', 'web-fragments'],
    entry_points={
        'xblock.v1': [
            'molecule_explorer = molecule_explorer_xblock.molecule_explorer:MOLECULE_EXPLORERolecule_explorerXBlock',
        ]
    },
    package_data={'molecule_explorer_xblock': ['static/**/**', 'templates/**/**']},
)
