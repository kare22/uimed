from setuptools import setup, find_namespace_packages
exec(open('silmused/version.py').read())

setup(
    name='silmused',
    version=__version__,
    license='MIT License',
    author='Karel Paan, Martti Kakk',
    author_email='paan.karel@gmail.com',
    packages=['silmused'],
    url='https://github.com/kare22/silmused',
    install_requires=[
        'psycopg2',
    ]
)