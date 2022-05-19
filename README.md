# meow

This is an example of how to use `setup.py` to make a Python package installable.

# Helpful links for setup.py things

- [Full `setup.py` file](https://github.com/pypa/sampleproject/blob/main/setup.py) with comments.
- https://packaging.python.org/guides/distributing-packages-using-setuptools/
- https://github.com/pypa/sampleproject

# Install from GitHub repository

At least two options:

1. Install using the `.tar.gz` of the project:

    ```
    pip install https://github.com/kaczmarj/minimal-setup.py-project/tarball/main
    ```

2. Install using `git` (requires `git` to be installed):

    ```
    pip install git+https://github.com/kaczmarj/minimal-setup.py-project
    ```

# Upload package to pypi.org

Note: See the [official documentation](https://packaging.python.org/en/latest/tutorials/packaging-projects/#generating-distribution-archives) for complete information.

Uploading the package to pypi.org makes it possible for others to `pip install NAME` the package.

This requires the packages `build` and `twine`: `pip install build twine`.

1. Build the package.

    ```
    python -m build
    ```

2. Upload the package. First, upload it to pypi's testing site. You can check if things look OK there.

    ```
    python3 -m twine upload --repository testpypi dist/*
    ```
    
    Then you can install it from the testing site, to make sure it works. Do this in a virtual environment.
    
    ```
    python3 -m venv venv-test
    source ./venv-test/bin/activate
    python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps meow-YOUR-USERNAME-HERE
    python3 -c "import meow"
    meow
    # Run any other tests you want.
    # Clean up the venv when you're finished.
    rm -r venv-test/
    ```

3. Once you're satisfied, upload it to the actual pypi site.

    ```
    python3 -m twine upload dist/*
    ```

# Choosing a license

See https://choosealicense.com/.
