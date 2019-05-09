from setuptools import find_packages, setup

# Where the magic happens:
setup(
    # name='configurer',
    # description='',
    # long_description=long_description,
    # long_description_content_type='text/markdown',
    # author='Jamie Lennox',
    # author_email='jamielennox@gmail.com',
    # url='https://github.com/jamielennox/configurer',
    packages=find_packages(exclude=["tests"]),
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    include_package_data=True,
)
