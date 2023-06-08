import os


def seed(path):
    """Filepath relative to test directory"""
    return os.path.join(os.path.split(os.path.realpath(__file__))[0], path)