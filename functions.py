import argparse

def create_parser():
    """ Creates the argument parser """
    parser = argparse.ArgumentParser(
        prog="Task Tracker",
        description="A CLI application built in python",
        formatter_class = argparse.ArgumentDefaultsHelpFormatter
    )
    
    return parser