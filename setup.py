from setuptools import setup

setup(
    name='fetch_prices',
    version='0.1',
    py_modules=['fetch_prices'],
    install_requires=[
        'Click',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        fetch_prices=fetch_prices:cli
    ''',
)
