from os.path import abspath, dirname, join, normpath
from setuptools import setup


setup(

	# Basic package information:
	name = 'aboki',
	version = '0.2',
	scripts = ('aboki', ),

	# Packaging options:
	zip_safe = False,
	include_package_data = True,

	# Package dependencies:
	install_requires = ['docopt>=0.6.2', 'requests>=2.13.0', 'beautifulsoup4>=4.5.3', 'html5lib>=0.999999999'],

	# Metadata for PyPI:
	author = 'Akinjide Bankole',
	author_email = 'r@akinjide.me',
	license = 'UNLICENSE',
	url = 'https://github.com/akinjide/aboki',
	keywords = 'forex cli utility fx currency abokifx aboki market rate',
	description = 'Black market currency rate instantly in your terminal!',
	long_description = open(normpath(join(dirname(abspath(__file__)), 'README.md'))).read()
)