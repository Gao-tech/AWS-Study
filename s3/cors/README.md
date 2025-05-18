## create a bucket

```
aws s3 mb s3://bucket-static-website-3333
```

## change block public access

```
aws s3api put-public-access-block \
    --bucket bucket-static-website-3333 \
    --public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=false,RestrictPublicBuckets=false"
```

## create a bucket policy

```
aws s3api put-bucket-policy --bucket bucket-static-website-3333 --policy file://policy.json
```

## Turn on static website hosting

```
aws s3api put-bucket-website --bucket bucket-static-website-3333 --website-configuration file://website.json
```

## Upload index html and include resourse cross orgin

```
aws s3 cp index.html s3://bucket-static-website-3333
```

## Applycors policy

## cors

```
aws s3api put-bucket-cors --bucket bucket-static-website-3333 --cors-configuration file://cors.json
```
