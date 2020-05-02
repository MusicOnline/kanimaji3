from setuptools import setup

requirements = []
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="kanimaji3",
    version="0.1.0",
    packages=["kanimaji3"],
    install_requires=requirements,
    python_requires=">=3.6.0",
    author="MusicOnline",
    description="Convert KanjiVG SVG into animated formats",
    license="MIT",
    keywords="kanjivg",
    url="https://github.com/MusicOnline/kanimaji3",
    project_urls={
        "Issue Tracker": "https://github.com/MusicOnline/kanimaji3/issues",
        "Documentation": "https://github.com/MusicOnline/kanimaji3",
        "Source Code": "https://github.com/MusicOnline/kanimaji3",
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities",
    ],
)
