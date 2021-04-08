#!/bin/bash

# do a  "bash ./s3cript.sh"  to run this file

#   batch upload all files from this dir to bucket
#aws s3 sync ./ s3://casinos-server-cashout 

#   create bucket
#aws s3 mb s3://casinos-server-cashout

#    Remove the s3script file from bucket
aws s3 rm s3://casinos-server-cashout/s3script.sh

#    copy file to created bucket
aws s3 cp norway-casinos-profit-data.txt s3://casinos-server-cashout

#    list the bucket contents or files files
aws s3 ls s3://casinos-server-cashout

#    Create an  temporary  http link to access file conten on browser for 30 seconds 
aws s3 presign s3://casinos-server-cashout/canada-casinos-profit-data.txt --expires-in 40


