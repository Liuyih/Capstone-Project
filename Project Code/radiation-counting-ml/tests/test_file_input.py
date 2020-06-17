from unittest.mock import Mock, mock_open, patch

from lib.ortec_file_utils import (
    with_parser,
    count_adc_events,
    get_file_contents,
)


class TestWithParser:
    def test_callable_called(self):
        mock = Mock()
        with open('data/cs.dat', 'rb') as file:
            with_parser(file, mock)
        mock.assert_called()

    def test_callable_max_calls(self):
        """
        Pass a callable that always returns False so with_parser iterates
        through the entire file
        """
        mock = Mock(return_value=False)
        with open('data/cs.dat', 'rb') as file:
            with_parser(file, mock)
        # TODO figure out why this is different than test_count_adc_events
        assert mock.call_count == 258559

    def test_callable_min_calls(self):
        mock = Mock(return_value=True)
        with open('data/cs.dat', 'rb') as file:
            with_parser(file, mock)
        mock.assert_called_once()


def test_count_adc_events():
    cs_adc_event_count = count_adc_events("data/cs.dat")
    assert cs_adc_event_count == 258556


def test_get_file_contents():
    # TODO don't hardcode this
    read_data = b'98vklml1kj98vjvalkj39f8j'
    m = mock_open(read_data=read_data)
    with patch('builtins.open', m):
        contents = get_file_contents('')
        assert contents == read_data
