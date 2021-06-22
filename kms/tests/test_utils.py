import pytest

from kms.utils import utils


def test_get_default_key_policy(kms_client):
    my_client = utils.get_default_key_policy("123456789012")
    acct_id = my_client.get_aws_acct_id()
    assert acct_id == '123456789012'


def test_get_aws_acct_id_fail(sts_client):
    my_client = Utils()
    acct_id = my_client.get_aws_acct_id()
    assert acct_id != '888888888888'

