import os
from setuptools import setup, find_packages
from pip.req      import parse_requirements
from pip.download import PipSession


# import the data inside package/info.py file, without trigger the
#  importing of the whole powergrasp package.
#  equivalent to the python2 execfile routine.
INFO_FILE = 'tergraw/info.py'
with open(INFO_FILE) as fd:
    code = compile(fd.read(), INFO_FILE, 'exec')
    local_vars = {}
    exec(code, {}, local_vars)  # don't use global vars, save local_vars
    __pkg_name__ = local_vars['__name__']  # save the interesting data
    __version__ = local_vars['__version__']


# access to the file at the package top level (like README)
def path_to(filename):
    return os.path.join(os.path.dirname(__file__), filename)


# parse requirements.txt
install_reqs = parse_requirements(path_to('requirements.txt'),
                                  session=PipSession())
reqs = [str(ir.req) for ir in install_reqs]


setup(
    name = __pkg_name__,
    version = __version__,
    packages = find_packages(),
    include_package_data = True,  # read the MANIFEST.in file
    install_requires = reqs,

    author = "lucas",
    author_email = "lucas.bourneuf@laposte.net",
    description = "Draw graphs in terminal",
    long_description = open(path_to('README.mkd')).read(),
    keywords = "graph terminal draw",
    url = "https://github.com/Aluriak/tergraw",

    classifiers = [
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
