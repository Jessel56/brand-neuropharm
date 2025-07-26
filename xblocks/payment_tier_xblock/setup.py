from setuptools import setup, find_packages
setup(
    name='payment_tier_xblock',
    version='1.0.0',
    packages=find_packages(),
    install_requires=['XBlock', 'web-fragments'],
    entry_points={
        'xblock.v1': [
            'payment_tier = payment_tier_xblock.payment_tier:PAYMENT_TIERayment_tierXBlock',
        ]
    },
    package_data={'payment_tier_xblock': ['static/**/**', 'templates/**/**']},
)
