import setuptools
import os, re, subprocess, sys

with open("README.md", "r") as fh:
    long_description = fh.read()

# Rewrite all local paths in the markdown
# to the commit specific gitlab path.
commit_hash = subprocess.check_output(["git", "rev-parse", "--verify", "HEAD"]).decode("utf-8").strip("\r\n")
project_path = "yookoala/python-dnsquery";
commit_url_base = "https://github.com/{project_path}/commit/{commit_hash}/".format(project_path=project_path, commit_hash=commit_hash)
long_description = re.sub(
    r'\[(.+?)\]\((?!(http|https):\/\/)(.+?)\)',
    r'[\1](' + commit_url_base + r'\3)',
    long_description
)

# Determine package name and version
# from environment overrides, if any
name = os.getenv("PACKAGE_NAME")
if name is None:
    name = "dnsquery"

version = os.getenv("VERSION")
if version is None:
    version = "0.1.0"

# Run setup
setuptools.setup(
    name=name,
    version=version,
    scripts=[],
    author="Koala Yeung",
    author_email="koalay@gmail.com",
    description="A simple module to query DNS records of a domain name.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yookoala/python-dnsquery",
    project_urls={
        "Code": "https://github.com/yookoala/python-dnsquery",
        "Issue tracker": "https://github.com/yookoala/python-dnsquery/issues",
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Utilities",
    ],
    install_requires=[
        "dnspython>=2.4.2",
        "httpx>=0.24.1",
    ],
    python_requires=">=3.8",
 )
