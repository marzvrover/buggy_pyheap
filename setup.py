from setuptools import setup, find_packages

setup(
    name='buggy_pyheap',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    tests_require=[
        'pytest',
    ],
    author='Marz Rover',
    author_email='marzvrover@ieee.org',
    description='A puropsefully buggy heap implementation. Perfect for learning how to debug!',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/marzvrover/buggy_pyheap',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
