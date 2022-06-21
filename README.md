# Napari workshop (June 29, 2022)

**Note:** If you run into troubles during the installation, don't hesitate to ask a teacher for help 🤚🏽

# 1. Set-up

Start by downloading this repository. If you already use `git`, you can clone the repository to your local machine:

```
git clone https://github.com/MalloryWittwer/napari-workshop.git
```

If you don't already use `git`, you can download [the repository](https://github.com/MalloryWittwer/napari-workshop.git) as a zip
file, and then unzip it on your computer.

[Image - Downloading this repository]('resources\download_code.png')

After that, open a terminal window.

---
**Windows**: Open the `Anaconda Prompt` from your start menu.

**Mac OS**: Open `Terminal` (tip: search for it using `cmd` + `space`).

**Linux**: Open your terminal application.

---
    

Navigate to the `napari-workshop` directory from the command line using the `cd` command. For example:

```
cd ~/Downloads/napari-training-course
```

## Setting up your environment

We will install `napari` in a dedicated Python environment to avoid that it interferes with other Python projects you may have. To create a new environment form the command line, run:

```bash
conda create -y -n napari-tutorial -c conda-forge python=3.9
```

Then, activate the environment using:

```bash
conda activate napari-tutorials
```

You should now see `(napari-tutorials)` on the left of your command prompt, which indicates that your new environement (named *napari-tutorials*) is active.

Run the following commands to install `napari`, `scikit-image`, and `Jupyter notebooks`:

```
pip install "napari[all]" scikit-image notebook
```

If the process ran smoothly, you should be all set. To verify that your installation is working, try opening the Napari viewer by typing:

```bash
napari
```

This should launch an empty `napari` viewer in a separate window. It may take up to two minutes for the window to show up the first time you launch this command.

You should be able to open a `Jupyter notebook` from your terminal by typing:

```bash
jupyter notebook
```

Once the Jupyter Notebook opens in your web browser, you should see the following:

[Screenshot of the jupyter root]()

- `/toolbox`
- `Napari_Guide_Tutorial.ipynb` => example tutorial for using napari for watershed.


## Optional: running Jupyter notebooks from Visual Studio Code

As an alternative to the web browser, you can also run Jupyter notebooks directly from the VS Code text editor. For this, you should:
- Install VS Code.
- Install the Python and Jupyter extensions for VS Code.
- Select the right Python environment to run the notebook. You can do this by clicking on `Kernel` at the top-right of the notebook.

