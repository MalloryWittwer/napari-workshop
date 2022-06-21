# Napari workshop (June 29, 2022)

**Note:** If you run into troubles during the installation, don't hesitate to ask a teacher for help 🤚🏽

# 1. Set-up

Start by downloading this repository. If you already use git, you can use the
following command to clone this repository to your local machine:

```
git clone https://github.com/...
```

If you don't already use git, you can download the whole repository as a zip
file, which you can then unzip on your computer.

[Image of how to do that]

After that, you should navigate to the `napari-workshop` directory from the command line.

```
cd napari-training-course
```

## Setting up your environment

It is highly recommended to install it in a dedicated Python environment so to avoid that it interferes with other Python projects you may have.

You should already have downloaded and installed Anaconda. If that is not the case, [do it now]().

1. Open your terminal.
	- **Windows**: Open the "Anaconda Prompt" from your start menu
	- **Mac OS**: Open Terminal (you can search for it in spotlight - cmd + space)
	- **Linux**: Open your terminal application

2. Create a new environment from the command line:

```bash
conda create -n napari-tutorial python=3.9
```

3. Activate the environment:

```bash
conda activate napari-tutorials
```

You should now see `(napari-tutorials)` on the left of your command prompt, which indicates that your environement is active.

4. Napari can be installed like any other Python library: via `pip` or `conda`.Install napari and a few other libraries:

```
pip install "napari[all]" scikit-image
```

5. If the process ran smoothly, you should be all set. To verify that your installation is working, try opening the Napari viewer by typing:

```bash
napari
```

This should launch an empty napari viewer in a separate window.




6. You can open a jupyter notebook in your browser by typing:

```bash
jupyter notebook
```

Congratulations! You are all set. You can start by following our [tutorial]() or having a look at our [toolbox]().


## Spyder

Open a new project, select the downloaded directory.

## VScode

Or select the correct Python interpreter in VS Code by typing `Ctrl` + `P` => `Select Python Interpreter`.


We've already prepared this code for you. Try executing [basic.py](./exampls/basic.py) or [basic.ipynb](./examples/basic.ipynb) in the examples folder.


## Get inspired by a few examples

Have a look at the `examples` folder, try executing a few to have an idea of how napari works.
