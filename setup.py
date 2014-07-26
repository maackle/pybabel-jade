from distutils.core import setup

setup(
    name='pybabel-jade',
    version='0.1.0',
    author='Michael Douglas Dougherty',
    author_email='michael@lv11.co',
    packages=['pybabel_jade',],
    # scripts=['bin/stowe-towels.py','bin/wash-towels.py'],
    url='http://pypi.python.org/pypi/pybabel-jade/',
    license='LICENSE.txt',
    description='Jade extractor for PyBabel.',
    long_description=open('README.txt').read(),
    install_requires=[
        "pyjade==2.2.0",
        "six==1.7.3",
    ],
)