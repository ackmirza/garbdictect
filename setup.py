import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

packages=setuptools.find_packages(),

setuptools.setup(
	name="garbdictect",
	version="0.1.0",
	author="Akil Mirza",
	author_email="ack.mirza@gmail.com",
	description="plastic litter detection tool",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/ackmirza/garbdictect",
	packages=["garbdictect"],
	install_requires=[
		"opencv-python",
		"pandas",
		"exif",
		"gpxpy",
		"torch",
	],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: ",
		"Operating System :: Linux",
	],
)

