## Create a bucket

```
aws s3 mb s3://metadata-5432
```

## create a new file

```
echo "Hello, I am happy" >> hihi.txt
```

## Upload file with metadata

```
aws s3api put-object --bucket metadata-5432 --key hihi.txt --body hihi.txt --metadata Planet=Mars
```

## Get Metadata through head object

```
aws s3api head-object --bucket metadata-5432 --key hihi.txt
```
