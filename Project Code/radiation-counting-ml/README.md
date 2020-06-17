# Radiation Counting Using Machine Learning ![python-3.8](https://img.shields.io/badge/python-3.8-blue)

## Basic Usage

Requires Python version 3.8. If this is not available, it is suggested to install it using pyenv:
<https://github.com/pyenv/pyenv>

1. Follow the instructions to install pipenv here: <https://pipenv.pypa.io/en/latest/install/#installing-pipenv>. Make
   sure that pipenv is added to your `PATH` if installing using pip by following the instructions in the note under
   [this section](https://pipenv.pypa.io/en/latest/install/#pragmatic-installation-of-pipenv). If you don't want to add
   it to your path, replace `pipenv` with `python -m pipenv` in future instructions, making sure `python` corresponds
   with the version of pip used to install pipenv.

2. Install required dependencies with pipenv

   ```shell
   pipenv install
   ```

3. Run one of the classifiers

   ```shell
   pipenv run python [script]
   ```

   where `script` is one of the following:
   * [`serializer_test_NB.py`](./serializer_test_NB.py): Naive Bayes
   * [`serializer_test_tree.py`](./serializer_test_tree.py): Decision tree
   * [`serializer_test_NN.py`](./serializer_test_NN.py): Neural network

## Testing

Check static typing with mypy and run unit tests with pytest

```shell
make test
```

## Docker

This application can be deployed in a Docker container.

```shell
./docker.sh [script]
```

where `script` is defined the same as in the Basic Usage section.

## Run using WinPython

See the instructions in [docs/WinPython.md](./docs/WinPython.md)
