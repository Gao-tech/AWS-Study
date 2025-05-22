# import boto3

# s3 = boto3.client('s3')
# bucket = 'prefixes-5432'
# prefix = 'hello/'  # folder path

# response = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)

# for obj in response.get('Contents', []):
#     print(obj['Key'])