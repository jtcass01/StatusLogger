from setuptools import setup, find_packages

if __name__ == "__main__":
    readme = open("README.md", "r")
    long_description = readme.read()
    readme.close()

    setup(name="pylogger",
          version="0.1",
          author="Jacob Taylor Cassady",
          description="Timestamped and Colored Logging Module",
          long_description=long_description,
          long_description_content_type="text/markdown",
          url="https://github.com/jtcass01/PyLogger",
          packages=find_packages(),
          classifiers=[
              "Programming Language :: Python :: 3"
          ],
          python_requires=">=3.6")
