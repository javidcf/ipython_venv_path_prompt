About
-----

A simple extension to show the path and virtual environment, if any, of the
current interpreter. The extension attempts to detect both |venv|_ and
Anaconda_ environments, and shows it along with the path above the standard
IPython input prompt.

Installation
------------

Install as usual from PyPI:

::

    pip install ipython_venv_path_prompt

or from git:

::

    git clone http://github.com/jdehesa/ipython_venv_path_prompt.git
    cd ipython_venv_path_prompt/
    python setup.py install

The extension can be loaded from within an IPython session with
``import ipython_venv_path_prompt`. To load the extension automatically, edit
your IPython profile file. This file is located under your profile directory,
which by default is ``~/.ipython/profile_default``, but you can check the
exact location with the following command:

::

    ipython -c "import IPython; print(IPython.get_ipython().profile_dir.location)"

If there is no ``ipython_config.py`` file in that directory, create one. Then,
edit the file and add the extension name to the list of extensions to load on
startup. Your configuration file could look like this:

.. code-block:: python

    c = get_config()
    c.InteractiveShellApp.extensions = [
        'ipython_venv_path_prompt'
    ]

For more information about IPython configuration, see `Introduction to IPython
documentation`_.

.. |venv| replace:: ``venv``
.. _venv: https://docs.python.org/3/library/venv.html
.. _Anaconda: https://www.anaconda.com/
.. _Introduction to IPython documentation: https://ipython.readthedocs.io/en/stable/config/intro.html