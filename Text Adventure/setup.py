from setuptools import setup

setup(
    name="game",
    version="0.1.0",
    packages=["game"],
    entry_points={"console_scripts": ["game = game.__main__:main"]},
)
