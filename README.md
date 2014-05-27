# ImageSwipe

ImageSwipe is a command line tool that allows users to resize and compare two satellite or aerial images of a given scene.
This can be used to show temporal changes, for example, land cover changes between two seasons or urban development from year to year.
This can also be used to make qualitative comparisons between different band combinations e.g. a natural color image to a false-color infrared image.
An example of the change detection capabilities of this tool can be seen in [this article from NASA](http://earthobservatory.nasa.gov/IOTD/view.php?id=81368) (click on "View Image Comparison").
This article uses the same jQuery plug-in as ImageSwipe, however, ImageSwipe was not used to create this visualization.

ImageSwipe generates the HTML/CSS and links the JavaScript dependencies needed to create a change detection visualization.
Using the open-source programming environemnt Python, **it automatically creates a web page showcasing the comparison between any two remote sensing images.**

## Installation

ImageSwipe depends on the Python PIL library and was written for Python 2.7.
ImageSwipe includes the [beforeafter JavaScript plugin for jQuery](http://www.catchmyfame.com/2009/06/25/jquery-beforeafter-plugin/).
Installation is easy with [Python virtual environments](https://pypi.python.org/pypi/virtualenv) installed:

    source setup.sh

But, if you choose not to use `virtualenv`, you can just install PIL:

    pip install PIL

## Usage

    Usage: imageswipe.py [ARGUMENT] <path to first image> <path to second image>

    Required Argument:
    -r, --resize	Specify an image width.
    -o, --original	Keep original image size.

    Optional Argument:
    -h, --help	Display usage information. 

    NOTE: Images must be the same size.

## Acknowledgements

ImageSwipe was developed by [MichiganView](http://www.michiganview.org) with support from [the AmericaView program](http://www.americaview.org/) under FY13 funds.

![alt tag](MichiganView.gif)

