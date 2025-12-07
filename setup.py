import os, sys
import setuptools

descx = '''clipmac is clipbard copy tool '''

classx = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ]

includex = [    "*", "panglib/",
                "pedlib/", "pedlib/images", "pedlib/examples",
                "image.png", "clipmac_ubuntu.png"]

#import shutil
#shutil.copy("../README.md", "README.md")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Get version number  from the server support file:
fp = open("clipmac.py", "rt")
vvv = fp.read(); fp.close()
loc_vers =  '1.0.0'     # Default
for aa in vvv.split("\n"):
    idx = aa.find("VERSION ")
    if idx == 0:        # At the beginning of line
        try:
            loc_vers = aa.split()[2].replace('"', "")
            break
        except:
            pass

#print("loc_vers:", loc_vers) sys.exit()

deplist = ["pyvguicom"] ,

setuptools.setup(
    name="clipmac",
    version=loc_vers,
    author="Peter Glen",
    author_email="peterglen99@gmail.com",
    description=descx,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pglen/clipmac",
    classifiers=classx,
    include_package_data=True,
    packages=setuptools.find_packages(),
    scripts = ['clipmac.py'],
    package_dir = {
                  },
    #package_data={ "pedlib": doclist, },
    python_requires='>=3',
    install_requires=deplist,
    entry_points={
        'console_scripts': [
            "clipmac=clipmac:mainfunc",
            ],
        },
)

# EOF


