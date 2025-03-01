import boto3
import requests
import argparse
import os

def download_file(url,local_filename): #function that dowloads file
	response=requests.get(url)
	with open(local_filename,'wb') as file:
		file.write(response.content)

def upload_s3(file_name,bucket_name): #function that uploads local file to s3 bucket
	s3=boto3.client('s3',region_name="us_east_1")
	s3.upload_file(file_name,bucket_name,file_name)

def generate_presigned(bucket_name,file_name,expiration): #function that generates presigned url & creates s3 client
	s3=boto3.client('s3',region_name="us_east_1")
	url=s3.generate_presigned_url('get_object',Params={'Bucket':bucket_name,'Key':file_name},ExpiresIn=expiration)

def main(): #call 3 functions in order
	url = sys.argv[1]
	bucket = sys.argv[2]
    	expiration = int(sys.argv[3])

	local_filename = os.path.basename(url)
	download_file(url, local_filename)
	upload_s3(local_filename, bucket)
	generate_presigned(bucket, local_filename, expiration)

	print(f"Presigned URL:\n{presigned_url}")

if __name__ == "__main__":
    main()
