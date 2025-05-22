## make a bucket with a folder

```
aws s3 mb s3://prefixes-5432
```

## make a folder

```
aws s3api put-object --bucket prefixes-5432 --key "hello/"
```

## put object

```
aws s3api put-object --bucket prefixes-5432 --key "hello/prefix.txt" --body "prefix.txt"
```

## list all the files inside one folder

```
aws s3 ls s3://prefixes-5432/hello/ --recursive

aws s3api list-objects-v2 \
  --bucket prefixes-5432 \
  --prefix "hello/" \
  --query "Contents[].Key"

```

## run python sdk file

```
python3 -m venv venv
source venv/bin/activate

pip3 install boto3
python3 python_sdk.py

deactivate
```
