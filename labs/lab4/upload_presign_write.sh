#!/usr/bin/bash

FILE=$1
BUCKET=$2
EXPIRE=$3

aws s3 cp "$FILE" "s3://$BUCKET/" #upload file to s3 bucket

PRESIGNED_URL=$(aws s3 presign --expires-in "$EXPIRE" "s3://$BUCKET/$FILE") #generates a presigned url

echo "$PRESIGNED_URL"
