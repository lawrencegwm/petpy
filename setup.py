from setuptools import setup

setup(name="petpy",
      version="0.2",
      description="Petrophysics utilities",
      url="https://example.com/",
      author="Gordon LAwrence",
      author_email="gordon.g.lawrence@shell.com",
      license="Apache 2",
      packages=["petpy"],
      install_requires=["numpy",],
      tests_require=["pytest", "pytest-cov",],
      entry_points={
            "console_scripts": [
                  "gardner=petpy.__main__:main",
            ],
      }
      )