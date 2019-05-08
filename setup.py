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
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=[],
    extras_require={
        'yaml': ['yaml'],
    },
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    include_package_data=True,
    # license='MIT',
    # classifiers=[
    #     'License :: OSI Approved :: MIT License',
    #     'Programming Language :: Python',
    #     'Programming Language :: Python :: 2',
    #     'Programming Language :: Python :: 2.7',
    #     'Programming Language :: Python :: 3',
    #     'Programming Language :: Python :: Implementation :: CPython',
    # ],
)
