#!/usr/bin/python3

# -*-coding:utf-8 -*-

import os
import boto3
from botocore.exceptions import ClientError



ACCESS_KEY = 'AWS_ACCESS_KEY_ID'
SECRET_KEY =  'AWS_SECRET_ACCESS_KEY'

PRI_BUCKET_NAME ='temp-maveste-1'
TRANSIENT_BUCKET_NAME ='temp-maveste-2'

F1 = "covid19-data.txt"
F2 = "airports-weather-data.txt"
F3 = "flight-pattern-data.txt"

DIR = "data" # where to upload to

DOWN_DIR = "dwnload" # where to download to

""" A python script for working with AWS S3 """


# Creating an Upload function
def upload_file(bucket, directory, file, s3, s3path=None):
    
    file_path = directory + '/' + file
    remote_path = s3path
    
    if remote_path is None:
        remote_path = file
        
    try:
        s3.Bucket(bucket).upload_file(file_path, remote_path)
    except ClientError as ce:
        print('error', ce)
        
        
# Creating our Download file
def download_file(bucket, directory, local_name, key_name, s3):
    
    file_path = directory + '/' +  local_name
    
    try:
        s3.Bucket(bucket).download_file(key_name, file_path)
    except ClientError as ce:
        print('error', ce)
        
        
# Delete several files at once by building a list of objects.
def delete_files(bucket, keys, s3):
   
    objects = []
    
    for key in keys:
        objects.append({'Key' : key})
        
    try:
        s3.Bucket(bucket).delete_objects(Delete= {'Objects': objects})
    except ClientError as ce:
        print('error', ce)
  
        
# List objects in a bucket
def list_objects(bucket, s3):
    
    try:
        response = s3.meta.client.list_objects(Bucket=bucket)
        
        objects = []
        
        for content in response['Contents']:
            objects.append(content['Key'])
        print(bucket, 'contains', len(objects), 'files')
        return objects
        
    except ClientError as ce:
        print('error', ce)
        
# Copy files to A bucket
def copy_file(source_bucket, destination_bucket, source_key, destination_key, s3):
    
    try:
        source = {
            'Bucket': source_bucket,
            'Key': source_key
        }
        s3.Bucket(destination_bucket).copy(source, destination_key)
        
    except ClientError as ce:
        print('error', ce)
        
        
# Prevent Bucket to be access publicly
def prevent_public_access(bucket, s3):
    
    try:
        s3.meta.client.put_public_access_block(Bucket=bucket, 
        PublicAccessBlockConfiguration= {
            'BlockPublicAcls': True,
            'IgnorePublicAcls': True,
            'BlockPublicPolicy': True,
            'RestrictPublicBuckets': True
            
        } )
        
    except ClientError as ce:
        print('error', ce)
        
# # create a bucket
# def create_bucket(name, s3):
#     try:
#         bucket = s3.create_bucket(Bucket=name)
#     except ClientError as ce:
#         print
    

# create a bucket
def create_bucket(name, s3, secure=False):
    
    try:
        s3.create_bucket(Bucket=name)
    
        if secure:
            prevent_public_access(name, s3)
    except ClientError as ce:
    
        print('error', ce)
        
# Defined a pre-sign url function to allow user download a file from a bucket
def generate_download_link(bucket, key, expiration_seconds, s3):
    
    try:
        response = s3.meta.client.generate_presigned_url('get_object', Params={
            'Bucket' : bucket,
            'Key'    : key
        }, ExpiresIn=expiration_seconds)
        print(response)
        
    except ClientError as ce:
        print('error', ce)
        
        
# For deleting a bucket that is no longer needed.
def delete_bucket(bucket, s3):
    
    try:
        s3.Bucket(bucket).delete()
    
    except ClientError as ce:
        print('error', ce)

# ------------- Function calls ---------------        

def main():
    """ entry point """
    
    access = os.getenv(ACCESS_KEY)
    
    secret = os.getenv(SECRET_KEY)
    
    s3 = boto3.resource('s3')
    
    # call the generate Download Function
    #generate_download_link(PRI_BUCKET_NAME, F3, 30, s3)
    
    # call the create)bucket function
   # create_bucket(TRANSIENT_BUCKET_NAME, s3, True)
    
    #Call to delete the bucket
    delete_bucket(TRANSIENT_BUCKET_NAME, s3)
    
    # Call the upload function 
    # upload_file(PRI_BUCKET_NAME, DIR, F1, s3)
    # upload_file(PRI_BUCKET_NAME, DIR, F2, s3)
    # upload_file(PRI_BUCKET_NAME, DIR, F3, s3)
    
    
    # # call the download functions
    # download_file(PRI_BUCKET_NAME, DOWN_DIR, F3, F3, s3)
    # download_file(PRI_BUCKET_NAME, DOWN_DIR, F1, F1, s3)
    # download_file(PRI_BUCKET_NAME, DOWN_DIR, F2, F2, s3)
    
    # # call the delete functions
    # delete_files(PRI_BUCKET_NAME, [F1, F2, F3], s3)
    
    # call the copy_file()
    # copy_file(PRI_BUCKET_NAME, TRANSIENT_BUCKET_NAME, F1, F2, s3)
    
    # # call the list objects from the bucket
    # list_objects(TRANSIENT_BUCKET_NAME, s3)
      
    

if __name__ == "__main__":
    main() 