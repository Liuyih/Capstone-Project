import logging
import numpy as np

import matplotlib.pyplot as plt


def describe_current_counts(counts):
    """
    Log some facts about counts:
        number of nonzero channels
        which channel has max counts
        what max counts is
    """
    num_nonzero_channels = len(counts
                               [np.where(counts != 0)[0]]
                               )
    max_count = np.max(counts)
    index_max_channel = np.where(counts == max_count)

    logging.info(
            f"{num_nonzero_channels} channels with nonzero counts."
            f"\nMax count is {max_count} on channel(s) {index_max_channel}.")
    # logging.info(np.where(counts != 0)[0])
    # logging.info(counts[np.where(counts != 0)[0]])


def plot_init():
    """
    Can run at start to configure figure, not necessary though.
    """
    plt.figure(figsize=(15, 10))
    plt.yscale("log")
    plt.ion()
    plt.show()


def plot_counts(counts):
    """
    Clear current axes and draw new one using counts.
    """
    plt.cla()
    plt.yscale("log")
    plt.plot(range(len(counts)), counts)
    plt.draw()
    plt.pause(.01)
