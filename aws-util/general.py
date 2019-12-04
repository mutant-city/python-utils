import boto3


def list_regions():
    ec2 = boto3.client('ec2')
    response = ec2.describe_regions()
    return [item['RegionName'] for item in response['Regions']]


def list_availability_zones():
    ec2 = boto3.client('ec2')
    response = ec2.describe_availability_zones()
    print('Availability Zones:', response['AvailabilityZones'])
