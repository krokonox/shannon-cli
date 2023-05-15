from setuptools import setup

setup(
    name="entropy-cli",
    version="0.1.0",
    py_modules=["entropy", "cli"],
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "entropy = cli:calculate_entropy",
            "ent = cli:calculate_entropy",
            "shannon = cli:calculate_shannon_encoding",
        ],
    },
)
