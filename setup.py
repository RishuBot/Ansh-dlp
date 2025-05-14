from setuptools import setup

setup(
    name='ansh-api',
    version='0.1',
    description='ansh-api - A wrapper for yt-dlp',
    author='Anshu',
    author_email='anshppt19@gmail.com',
    packages=['ansh_api'],
    entry_points={
        'console_scripts': [
            'ansh-api = ansh_api.__main__:main'
        ]
    },
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
