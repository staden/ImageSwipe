ImageSwipe - View temporal changes with an image comparison tool for web applications

ImageSwipe is a command line tool that compares two similar images and makes the temporal changes between them appear evident. The goal of ImageSwipe is to provide a tool to researchers and web developers that could allow them to use geospatial imagery on a scale that can reach a wide audience, such as a web page. The image comparison uses catchmyfame.com's before/after plugin from http://www.catchmyfame.com/2009/06/25/jquery-beforeafter-plugin/

Step 1: Select your imagery.
Images must have the same aspect ratio for the tool to work. Images of the same height and width (and geographic footprint, or content) will yield the best results. Place the selected images into a working directory.


Step 2: Select the size of your output.
The command line tool is able to resize initial imagery to fit the desired space and resolution. The usage of this command is as follows:
imageswipe.py <ARGUMENT> <path to first image> <path to second image>

Required Argument:
-r, --resize    Specify an image width (in number of pixels).
-o, --original  Keep original image size.

Optional Argument:
-h, --help      Display usage information. 


Step 3: View and use your image comparison.
Open imageswipe.html in your browser to view the image comparison. If you wish to move this output, the contents of imageswipe.html depend on all files and subdirectories in the imageswipe package.


ImageSwipe is written in Python and relies on the sys, getopt, and PIL libraries.
ImageSwipe includes the Before/After Javascript plugin at http://www.catchmyfame.com/2009/06/25/jquery-beforeafter-plugin/

Sourced at:
https://github.com/staden/imageswipe

Related links:
http://apache.mtri.org:8080/display/miview/Resources+for+AmericaView

