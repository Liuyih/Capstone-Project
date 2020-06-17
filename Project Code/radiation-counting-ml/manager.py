from datetime import datetime, timedelta
import logging
import os
import time

# from interface import plot_init, plot_counts
from lib.ortec_file_utils import get_listPRO_output_file_path
from lib.serializer import Serializer


def watch_file(file_path, process_file=None, plot_counts=None):
    """
    Watch a file for changes until nothing happens for 3 seconds.
    On each change, call functions if passed: process_file(), plot_counts().

    Can also just probably use watchdog.observers.polling stuff.
    (If using watchdog.observers.Observer, it won't
    call on_modified unless you either close file or open
    explorer.exe properties dialog for file, which triggers something)
    So just querying file manually.
    """

    start_time = datetime.utcnow()
    file_size = 0
    file_size_changes = 0

    last_change_time = 0

    while True:
        new_size = os.path.getsize(file_path)
        if new_size != file_size:
            file_size = new_size

            now = datetime.utcnow()
            last_change_time = now
            file_size_changes += 1
            logging.info(f"==Change #: {file_size_changes}\t"
                         f"New size: {new_size}\t"
                         f"Time elapsed: {now - start_time}")

            if process_file:
                counts = process_file()

                if plot_counts:
                    plot_counts(counts)
        else:
            delta = datetime.utcnow() - last_change_time

            if delta > timedelta(seconds=3):
                logging.info(
                        f"No changes to {file_path} for 3 seconds, exiting.")
                return

        # arbitrary 1 ms wait to check for file change
        time.sleep(.001)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s.%(msecs)03d '
                        '%(levelname)s:\t%(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # start directory watching
    listPRO_file_path = get_listPRO_output_file_path()
    serializer = Serializer(listPRO_file_path)

    # plot_init()
    # Now that we have .dat path, just watch size continuously
    watch_file(listPRO_file_path, process_file=serializer.serialize)
