from setuptools import setup

setup(
    name="ipython_venv_path_prompt",
    version="0.1",
    packages=["ipython_venv_path_prompt"],
    license="MIT",
    author="Javier Dehesa",
    author_email="javidcf@gmail.com",
    url="http://www.github.com/jdehesa/ipython_venv_path_prompt",
    description="IPython magic to reverse a string",
    long_description=open("README.rst").read(),
    keywords="ipython venv virtualenv path cwd prompt",
    install_requires = ['ipython'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Framework :: IPython",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Utilities",
    ],
)
