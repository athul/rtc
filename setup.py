from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in rtc_app/__init__.py
from rtc_app import __version__ as version

setup(
	name="rtc_app",
	version=version,
	description="RTC is a cms for Bus Ticketing and Services",
	author="Foo Fighters",
	author_email="athul8720@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
