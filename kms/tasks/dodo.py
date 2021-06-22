from kms.utils import utils as kms_utils
from tool.utils import utils as tool_utils
from sts.utils import utils as sts_utils


def task_kms_key_params():

    account_id = sts_utils.Utils().get_aws_acct_id()
    key_policy = kms_utils.get_default_key_policy(account_id)
    user_name = tool_utils.get_user_name()

    def show_params(bucket_name):
        if bucket_name is None:
            raise ValueError("KMS key name must be defined.")
        else:
            print(bucket_name)
            print(key_policy)
            print(user_name)

    return {'actions': [show_params],
            'params': [{'name': 'bucket_name',
                        'long': 'bucket_name',
                        'short': 'b',
                        'default': None,
                        'type': str}],
            'verbosity': 2,
            }


def task_create_kms_key_template():

    account_id = sts_utils.Utils().get_aws_acct_id()
    key_policy = kms_utils.get_default_key_policy(account_id)
    user_name = tool_utils.get_user_name()




