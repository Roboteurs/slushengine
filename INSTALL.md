Installation Instructions
=========================

Currentley the Slush hardware driver has been created for Python 3.x. Installing the Slush Python module is very simple, however there are some pre-requisites that are required in order for the Slush module to work. The Slush driver requires full control over the Raspberry Pi's I2C, SPI, and GPIO drivers. These are hardware interfaces on the Raspberry Pi that allow comunication with the hardware on the SlushEngine hardware.

Pre-Requisites
--------------

First we need to enable the SPI and I2C interfaces on the Raspberry Pi. This has been documented on the Raspberry Pi webpage and many other forums. The link below is a simple description of how these interfaces can be anabled for use.

[Enable SPI and I2C interface](https://blogs.oracle.com/atael/entry/i2c_and_spi_on_raspberry)

Once the interfaces have been enabled we can begin to install the Python packages that are used to communicate with these interfaces. If it is not already installed install Pip. This is an installer tool that can be used to install a very large number of Python packages from a variety of sources.

>$sudo apt-get install python3-pip

Then we can install the spidev library. This library makes comunciation between Python and the SPI interface very simple.

>$ pip-3.2 install spidev

[Spidev python library](https://pypi.python.org/pypi/spidev)

The next step is to install the I2C python libraries. Quick2Wire does an excellent job of including device drivers in there I2C library while still allowing low level hardware functionallity. The installation instructions and source can be found at the link below.

[Quick2wire instalation and API](https://github.com/quick2wire/quick2wire-python-api)

Installation
------------

Once all of the above packages are installed you can install the Slush library. First you will need a copy of the Slush source. You can clone the repository or you can download and uncompress the zip package.

Once the package is uncompressed you can navigate into the top directory of the repository.

>$ cd Slush-Engine

When you are inside this directory then use the following command to install the Slush library

>$ python3 setup.py install

To test if the Slush library installed correctly open a terminal and import the Slush library

>import slush


We are trying hard to make this installation more streamline. We ask that any issues you encounter during the installation you post as an issue on git or email reinerschmidt@roboteurs.com