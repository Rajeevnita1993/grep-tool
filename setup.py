from setuptools import setup, find_packages

setup(
    name='grep_tool',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'grep=grep_tool.my_grep:main',
        ],
    },
    author='Rajeev Kumar',
    author_email='rajeevnita29@gmail.com',
    description='A custom grep tool in Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_grep_tool',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
