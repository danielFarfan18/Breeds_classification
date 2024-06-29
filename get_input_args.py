#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: Daniel Farfán
# DATE CREATED: 25/06/2024                 
# REVISED DATE: 
# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse
import os 
import sys

# TODO 1: Define get_input_args function below please be certain to replace None
#       in the return statement with parser.parse_args() parsed argument 
#       collection that you created with this function
# 
def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to created and defined these 3 command line arguments. If 
    the user fails to provide some or all of the 3 arguments, then the default 
    values are used for the missing arguments. 
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object  
    """
    # Create Parse using ArgumentParser
    parser = argparse.ArgumentParser()
    # Create 3 command line arguments as mentioned above using add_argument() from ArguementParser method
    parser.add_argument('--dir', type = str, default = 'pet_images/', help = 'path to the folder of pet images')
    parser.add_argument('--arch', type = str, default = 'resnet', help = 'CNN model architecture to use')
    parser.add_argument('--dogfile', type = str, default = 'dognames.txt', help = 'text file with dog names')
    
    return parser.parse_args()


def check_command_line_arguments(in_arg):
    """
    Checks the validity of command line arguments.
    
    Parameters:
        in_arg: ArgumentParser object containing command line arguments.
        
    Returns:
        None
    """
    # Check if the image directory exists
    if not os.path.isdir(in_arg.dir):
        print("Error: The directory {} does not exist.".format(in_arg.dir))
        sys.exit(1)  # Exit the program if the directory does not exist
    
    # Check if the dogfile exists
    if not os.path.isfile(in_arg.dogfile):
        print("Error: The dog names file {} does not exist.".format(in_arg.dogfile))
        sys.exit(1)  # Exit the program if the dogfile does not exist
    
    # Check if the architecture argument is one of the supported architectures
    supported_architectures = ['resnet', 'alexnet', 'vgg']
    if in_arg.arch not in supported_architectures:
        print("Error: The architecture {} is not supported.".format(in_arg.arch))
        print("Supported architectures are: vgg, alexnet, resnet")
        sys.exit(1)  # Exit the program if the architecture is not supported