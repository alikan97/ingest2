import boto3
import os
class KinesisClient:
    def __init__(self, stream_name):
         self.streamName = stream_name
         self.client = boto3.client('kinesis',
                            region_name = os.environ.get('REGION'),
                            aws_secret_access_key = os.environ.get('SECRET'),
                            aws_access_key_id = os.environ.get('ACCESS'))

    def put(self, data, partition_key):
         print(data)
     #    return self.client.put_record(
     #         StreamName = self.streamName,
     #         Data = data,
     #         PartitionKey = partition_key
     #    )