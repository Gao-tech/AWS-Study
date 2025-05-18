from aws_cdk import (
    Stack,
    aws_s3 as s3
)
from constructs import Construct

class PythonCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # ✅ Create an S3 bucket
        s3.Bucket(self, "MycdkBucket",
        )
