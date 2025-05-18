## Crate a bucket

## Public access

```
aws s3api put-public-access-block --bucket encripted-bucket-333 --public-access-block-configuration BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=false,RestrictPublicBuckets=fals
```

## Access Policy

```
aws s3api put-bucket-policy --bucket encripted-bucket-333 --policy file://policy.json
```

## Upload file

```
echo "hello hei" >>hello.txt
```

```
aws s3 cp hello.txt s3://encripted-bucket-333
```

## Upload file with KMS

```
echo "encript file" >>encriptedfile.txt
```

```aws s3api put-object --bucket encripted-bucket-333 --key encriptedfile.txt --body encriptedfile.txt --server-side-encryption aws:kms --ssekms-key-id 4a0ca863-6f20-4f0c-8537-aa6a749832ca

```

## make sse key

```
openssl rand -out ssec.key 32
```

```
aws s3 cp hello.txt s3://encripted-bucket-333/helloen.txt \
--sse-c AES256 \
--sse-c-key fileb://ssec.key
```

## download the file with the key

```
aws s3 cp s3://encripted-bucket-333/helloen.txt . --sse-c AES256 --sse-c-key fileb://ssec.key
```
