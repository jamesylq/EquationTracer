# What is EquationTracer?
EquationTracer uses NumPy and Pygame to convert an arbitrary scribble into a parametric equation which you can plot on Graphing Calculators such as Desmos!

## Installation
This is a guide on how to install EquationTracer.
>**Note**: You need Python installed on your system, along with either pip or pipx.

If you do not want to use pip or pipx, you can also alternatively clone this git repository, or simply copy the code!

Linux: `pip install equationtracer`

Mac: `pip3 install equationtracer`

Windows (pipx): `pipx install equationtracer`

Windows (pip): `pip install equationtracer`

>**Note**: For Windows, it is recommended to use pipx as using pip does not allow the poetry script `trace-equation` to run, but pipx does support this. If pip is used, you need to run the program with the other command, as provided below. On Max and Linux, pip3 will automatically allow the poetry script `trace-equation` to be able to be executed.

## Running
To run the program, type into a command line: `trace-equation`

If you installed the program with pip (instead of pipx) on windows, or if the above command doesn't work, you can also do:

Windows: `py -m equationtracer`

Others: `python3 -m equationtracer`

## Updating

To update the program, use the following:

Linux: `pip install -U equationtracer`

Mac: `pip3 install -U equationtracer`

Windows (pipx): `pipx upgrade equationtracer`

Windows (pip): `pip install -U equationtracer`

## Dependencies

EquationTracer uses the libraries numpy, pygame and pyperclip, and runs on Python 3.9 and above.