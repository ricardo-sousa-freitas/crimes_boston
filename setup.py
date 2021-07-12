from setuptools import setup, find_packages
#from requirements import required

PACKAGE_NAME = "boston_crimes"

setup(name=PACKAGE_NAME,
    packages=find_packages(),
    entry_points={'console_scripts': [f'{PACKAGE_NAME} = {PACKAGE_NAME}.main:print_test']}),
    # install_requires = ["numpy==1.14.5",
    #             "pandas==0.24.2"])