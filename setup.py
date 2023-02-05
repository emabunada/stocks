from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in stocks/__init__.py
from stocks import __version__ as version

setup(
	name="stocks",
	version=version,
	description="new stocks app",
	author="mohammed",
	author_email="e.mabunada@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
