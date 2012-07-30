pysvg2font
==========

Python scripts to automate the process of converting a list of svg vectorial 
graphics to ttf fonts.

pysvg2font uses the fontforge python bindings to generate True Type Font (ttf) 
files based on a list of .svg files.

The idea behind it is simplicity to obtain easily scalable monochrome icons
which can be used via css in html files in a similar way 
[github defines in its styleguide](https://github.com/styleguide/css/7.0) 

A summary the features of pysvg2font are:
 * Generate .ttf files from .svg files (beta)
 * Generate .css files which define classes for the icons based on the .svg file
   names (not implemented)
 * Define different sizes for the icons in the .css files (not implemented) 
 * Generate .html files with a preview of all the icons in different sizes (not
   implemented)

Requirements
------------

Requires fontforge python module, which is currently only available from the
ubuntu repositories, so at the moment the only platform supported for pysvg2
font is ubuntu linux. To install fontforge:

<pre>
 $ sudo apt-get install python-fontforge
</pre>

Another dependency is the python module `jinja2` which is used as template
engine to generate the css, scss and html.

Examples
--------

Some sample .svg files can be found under the directory `examples/icons/svg`. 
They have been taken from the [Entypo](http://www.entypo.com/) font by Daniel
Bruce (CC BY-SA license)

To simply generate the .ttf file from the directories containing .svg files

<pre>
 $ python -m pysvg2font examples/icons/svg/action/ examples/icons/svg/object/ examples/css/pysvg2font_sample.ttf
</pre> 

How to use
----------

Here is a dump of the help for the command line tool:

<pre>
usage: python -m pysvg2font [-h] [--scss-output]
                            [--css-output-path CSS_OUTPUT_PATH]
                            [--html-output-path HTML_OUTPUT_PATH]
                            [--icon-size ICON_SIZE [ICON_SIZE ...]]
                            svg_source_directory [svg_source_directory ...]
                            output_ttf

Generates ttf files based on monochrome SVG files and generates stylesheets to
use the fonts as vectorial icons in HTML pages.

positional arguments:
  svg_source_directory  source directory path (absolute or relative). The
                        directory must contain svg icons. When generating the
                        css classes for the icons, the directory name will be
                        used as prefix
  output_ttf            path (absolute or relative) to output .ttf file

optional arguments:
  -h, --help            show this help message and exit
  --scss-output         generates scss file which can be included from other
                        scss scripts. It will be created in the same directory
                        as the output .ttf file and will have. The filename
                        will be the .ttf basename + _icons.scss
  --css-output-path CSS_OUTPUT_PATH
                        generates css file with the icon class descriptions.
                        An argument is needed for the path where to create the
                        css file
  --html-output-path HTML_OUTPUT_PATH
                        generates a basic html file wich includes the style
                        for the icons and renders all the svg icons including
                        the alphanumeric character, character code and css
                        class for every icon next to a sample of every icon in
                        the different sizes generated
  --icon-size ICON_SIZE [ICON_SIZE ...]
                        list of comma separated integer,name values which will
                        be used to generate classes for icons for different
                        sizes, valid examples could be 16,small 32,medium
                        64,large This applies only when "--scss-output",
                        "--css-output-path" or "--html-output-path" are
                        enabled
</pre>