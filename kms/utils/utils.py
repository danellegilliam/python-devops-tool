def get_default_key_policy(account_id):
    """

    :param account_id: aws account id
    :type account_id: str
    :return: default aws kms key policy
    :rtype: json
    """
    policy = f"""
    {{
        "Version": "2012-10-17",
        "Id": "key-default-1",
        "Statement": [
            {{
                "Sid": "Enable IAM User Permissions",
                "Effect": "Allow",
                "Principal": {{
                    "AWS": "arn:aws:iam::{account_id}:root"
                }},
                "Action": "kms:*",
                "Resource": "*"
            }}
        ]
    }}
    """
    return policy

