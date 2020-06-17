# Instructions for using WinPython

## Setup
This project uses Python 3.8. The following instructions show how to use WinPython to set up a portable Python
environment that can be set up in a self contained folder that can be copied for use on a different computer.

This guide uses a flash drive mounted as `E:\`
(if using WSL, need to mount drive with `sudo mount -t drvfs E: /mnt/e -o metadata` to be able to run `git clone`,
because the clone uses chmod)

### Get project files
Run 
```shell
cd E:\
git clone https://github.com/ianbrown9475/radiation-counting-ml.git
```

Add in existing Ortec ListPRO `.dat` files to `E:\radiation-counting-ml\data` folder if using existing data.

### Winpython setup on flash drive
[WinPython setup download](https://github.com/winpython/winpython/releases/tag/2.2.20191222). We recommend using the
`dot` version, which contains only the needed Python binaries and so is 23 MB as opposed to over 500 MB. The following
binary was used during this guide's creation: `Winpython64-3.8.1.0dot.exe`.

Open `Winpython64-3.8.1.0dot.exe`. Select the flash drive `E:\` as the destination folder, and finish setup with the
default options selected. After setup, the WinPython prompt should now be at `E:\WPy64-3810\WinPython Powershell
Prompt.exe`

Open the WinPython prompt.

Check that WinPython pip is the one in use by looking at the path returned here:

```shell
pip --version
``` 

After verifying correct pip is in use, install pipenv:

```shell
pip install pipenv
```

### Project dependency installation
Install packages that are listed in Pipfile:

```shell
cd E:\radiation-counting-ml\
pipenv install
```

Installation done.

## Running project
The project can be run at the WinPython prompt:

```shell
cd E:\radiation-counting-ml\
pipenv run python manager.py
```

The program is now watching the folder `E:\radiation-counting-ml\data\` for files from ListPRO. Start writing to a
`.dat` file there with ListPRO, and the program will start trying to determine the isotopes in the spectrum, and return
a classification after the confidence value is reached.

To simulate ListPRO with the existing ListPRO output file `cs.dat`, open another WinPython prompt and run:

```shell
pipenv run python listpro_simulator.py data/cs.dat
```

This writes the contents of `data/cs.dat` incrementally to `data/testfile.dat`.
