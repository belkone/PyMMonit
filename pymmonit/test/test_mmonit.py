import pytest
import pymmonit


@pytest.fixture
def requests(mocker):
    return mocker.patch('pymmonit.mmonit.requests')


def test_basic(requests):
    mm = pymmonit.MMonit('URL', 'username', 'password')
    mm.hosts_list()
    mm.map_rangeids()
