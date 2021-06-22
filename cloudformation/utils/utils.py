import boto3


class Utils:

    def __init__(self):
        self.sts = boto3.client("cloudformation")

    def create_stack(self):

    def get_aws_acct_id(self):
        """

        :return: aws account id
        :rtype: str
        """
        account_id = self.sts.get_caller_identity()["Account"]
        return account_id

