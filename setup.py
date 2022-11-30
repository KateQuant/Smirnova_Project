# It should work with the sys.argv, but unfortunately doesn't work. I used not pretty way to ask for arguments through
# PYTHONPATH=./ in comandline
from setuptools import setup, find_packages

setup(
    name="qpa_final_project",
    version="1.0",
    packages=find_packages(),
)
