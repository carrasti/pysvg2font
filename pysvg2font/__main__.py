#!/usr/bin/env python

import argparse

from pysvg2font import SvgToFontGenerator

def parse_args(args=None):
    # TODO: the argparse usage line is wrong, Python issue #15433
    parser = argparse.ArgumentParser(description='Generates ttf files based on monochrome SVG files and generates stylesheets to use the fonts as vectorial icons in HTML pages.',
                            prog='python -m pysvg2font')
    
    parser.add_argument('--scss-output',
                        help='generates scss file which can be included from other scss scripts. It will be created in the same directory as the output .ttf file and will have. The filename will be the .ttf basename + _icons.scss',
                        action='store_true')
    parser.add_argument('--css-output-path',
                        help='generates css file with the icon class descriptions. An argument is needed for the path where to create the css file',
                        nargs=1)
    parser.add_argument('--html-output-path',
                        help='generates a basic html file wich includes the style for the icons and renders all the svg icons including the alphanumeric character, character code and css class for every icon next to a sample of every icon in the different sizes generated',
                        nargs=1)
    parser.add_argument('--icon-size',
                        help='list of comma separated integer,name values which will be used to generate classes for icons for different sizes, valid examples could be 16,small 32,medium 64,large\n This applies only when "--scss-output", "--css-output-path" or "--html-output-path" are enabled',
                        nargs="+",
                        default=["16,small", "32,medium", "64,large"])
    parser.add_argument('svg_source_directory',
                        help='source directory path (absolute or relative). The directory must contain svg icons. When generating the css classes for the icons, the directory name will be used as prefix',
                        nargs='+')
    parser.add_argument('output_ttf',
        help='path (absolute or relative) to output .ttf file')
    
    return parser.parse_args(args)


if __name__ == '__main__':
    args = parse_args()
    
    fontgenerator=SvgToFontGenerator(args.svg_source_directory,
                                     args.output_ttf)
    
    fontgenerator.generate()