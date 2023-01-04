from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name="alta",
    version="0.0.1",
    author="SpyGuy",
    author_email="shashankprasanna1@gmail.com",
    license="GNU GPLv3",
    description="A command line tool utilizing CHAT-GPT to solve problems and answer questions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SpyGuy0215/alta",
    py_modules=["alta", "app"],
    packages=find_packages(),
    install_requires=[requirements],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        alta=alta:cli
    '''
)