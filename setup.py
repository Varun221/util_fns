from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='util_fns',
    url='https://github.com/jladan/util_fns',
    author='YV',
    author_email='',
    packages=['util_fns'],
    # Needed for dependencies
    install_requires=['matplotlib'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='utility functions useful for day-to-day work',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),d
)