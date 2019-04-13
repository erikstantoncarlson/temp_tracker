from setuptools import setup

setup(
	name="temp_tracker",
	version="0.1",
	description="Tracks temperatures and gets their stats.",
	url="https://github.com/erikstantoncarlson/temp_tracker",
	author="Erik Carlson",
	author_email="erikstantoncarlson@gmail.com",
	license="MIT",
	packages=["temp_tracker"],
	test_suite="tests",
	zip_safe=False
)