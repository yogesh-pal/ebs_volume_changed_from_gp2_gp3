import json
import boto3

def get_volume_name_from_arn(volume_arn):
    #split the arn using column (":"") seprator
    arn_parts = volume_arn.split(":")
    #THe volume id is the last part of the ARN after the 'volume' prefix
    volume_id = arn_parts[-1].split('/')[-1]
    return volume_id
    
def lambda_handler(event, context):
    
    volume_arn = event['resources'][0]
    volume_id = get_volume_name_from_arn(volume_arn)
    
    ec2_client = boto3.client('ec2')

    response = ec2_client.modify_volume(
        VolumeId=volume_id,
        VolumeType='gp3',
)
 