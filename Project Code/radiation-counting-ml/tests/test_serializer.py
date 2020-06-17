import numpy as np

from lib.serializer import Serializer


class TestSerializer:
    def test_serialize(self):
        serializer = Serializer('data/cs.dat')
        counts = serializer.serialize()
        nonzero_channel_count = len(np.nonzero(counts)[0])
        assert nonzero_channel_count == 3670
