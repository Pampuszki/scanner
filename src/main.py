import os

from logger import logger
from scan.scan import Scan
from utils.utils import check_dir_exist


def main():
    """The main function."""
    data_dir = os.path.join(os.getcwd(), "data")
    check_dir_exist(data_dir)
    # scanner = Scan()
    logger.info("Calculate finished")
    return 0


if __name__ == "__main__":
    main()
