from setuptools import setup, find_packages

setup(
    name='init_flask',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'init_flask'
    ]
)
