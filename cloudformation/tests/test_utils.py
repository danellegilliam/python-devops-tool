import pytest

from sts.utils.utils import Utils


def test_get_aws_acct_id_pass(sts_client):
    my_client = Utils()
    acct_id = my_client.get_aws_acct_id()
    assert acct_id == '123456789012'


def test_get_aws_acct_id_fail(sts_client):
    my_client = Utils()
    acct_id = my_client.get_aws_acct_id()
    assert acct_id != '888888888888'

