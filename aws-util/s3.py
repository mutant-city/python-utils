""" 
A utility module for working with s3 
Note: credentials must be set in ~/.aws
"""
import boto3, botocore, time


def to_string(location, separator="|"):
    """ 
    Returns an s3 object as string.
    Location parameter is a multipart string of bucket | object key.
    ex: 'thisis.somebucket.ap-southeast-1|deploy/testfile.json'
    """
    location = location.split(separator)
    s3 = boto3.resource('s3')
    return s3.Object(location[0], location[1]).get()["Body"].read()


# good bucket exists resource:
# https://stackoverflow.com/questions/26871884/how-can-i-easily-determine-if-a-boto-3-s3-bucket-resource-exists
def bucket_exists_v1(bucket_name):
    try:
        s3 = boto3.resource('s3')
        s3.meta.client.head_bucket(Bucket=bucket_name)
        return True
    except:
        # raise (f"The bucket {bucket_name} does not exist or you have no access.")
        return False


def bucket_exists_v2(bucket_name):
    s3 = boto3.resource('s3')
    return s3.Bucket(bucket_name) in s3.buckets.all()


def bucket_exists_v3(bucket):
    s3 = boto3.resource('s3')
    try:
        s3.meta.client.head_bucket(Bucket=bucket)
        print(f"Bucket Exists! {bucket}")
        return True
    except botocore.exceptions.ClientError as e:
        # If a client error is thrown, then check that it was a 404 error.
        # If it was a 404 error, then the bucket does not exist.
        error_code = int(e.response['Error']['Code'])
        if error_code == 403:
            print("Private Bucket. {bucket} Forbidden Access!")
            return True
        elif error_code == 404:
            print(f"Bucket Does Not Exist! {bucket}")
            return False


# note: oddly certain regions seem to require the region_name to do objects.all() call? i.e. ap-northeast-1
def purge_bucket(bucket, region):
    s3 = boto3.resource('s3', region_name=region)
    if bucket_exists_v3(bucket):
        bucket = s3.Bucket(bucket)
        bucket.objects.all().delete()


def create_bucket_if_not_exists(bucket, region):
    out = f"Creating {bucket} in {region}"
    print(out)

    if not bucket_exists_v3(bucket):
        s3 = boto3.resource('s3', region_name=region)
        # https://github.com/boto/boto3/issues/125 (us-east-1 is the 'default')
        if region == 'us-east-1':
            s3.create_bucket(Bucket=bucket)
        else:
            s3.create_bucket(
                Bucket=bucket,
                CreateBucketConfiguration={
                    'LocationConstraint': region
            })
        print(f"Created bucket: {bucket}.")

    # wait to ensure bucket existence
    while not bucket_exists_v3(bucket):
        x = 1
        print(f"Bucket is still being created. Waiting for {x} seconds.")
        time.sleep(x)
