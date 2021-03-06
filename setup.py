from setuptools import find_packages, setup

setup(
    name="pt2bs",
    description="Python to binary build system based on nuitka.",
    version="0.2.0",
    license="MIT",
    author="ssleert",
    author_email="ssleert@gmail.com",
    url="https://github.com/unxsh/pt2bs",
    packages=find_packages(),
    install_requires=["nuitka"],
    keywords=["python", "nuitka", "pbs", "compiler", "exe", "bin", "build"],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X"
    ],
)
