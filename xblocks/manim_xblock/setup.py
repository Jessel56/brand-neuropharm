from setuptools import setup, find_packages
setup(
    name='manim_xblock',
    version='1.0.0',
    packages=find_packages(),
    install_requires=['XBlock', 'web-fragments'],
    entry_points={
        'xblock.v1': [
            'manim = manim_xblock.manim:MANIManimXBlock',
        ]
    },
    package_data={'manim_xblock': ['static/**/**', 'templates/**/**']},
)
