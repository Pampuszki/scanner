import os


def check_dir_exist(path: str):
    """
    Chceck if directory exist if not create it.

    Args:
        path (str): Path to directory.
    """
    if not os.path.exists(path):
        os.makedirs(path)
