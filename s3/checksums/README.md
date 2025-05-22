## Create a new s3 bucket

```
aws s3 mb s3://checksums-examples-ab-5432
```

## Create a file that we will do a checksum

```
echo "hello earch" > checksumfile.txt
```

## checksum for md5 algorithm on Macbook

```
md5 checksumfile.txt
# c186b6903296dcde10184c269e23d5a9
```

## upload the file to s3, met issue that put-object

```

aws s3api put-object --bucket checksums-examples-ab-5432 --key checksumfile.txt --body checksumfile.txt

aws s3api head-object --bucket checksums-examples-ab-5432 --key checksumfile.txt
```

## "ETag": "\"b32b94154afc05d4a74ee3ddb76bb595\"
