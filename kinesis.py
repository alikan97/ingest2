import boto3
import os
import json
from logger import withLogging

class KinesisClient:
    def __init__(self, stream_name, devMode: bool):
         self.streamName = stream_name
        #  self.client = boto3.client('kinesis',
        #                     region_name = os.environ.get('REGION'),
        #                     aws_secret_access_key = os.environ.get('SECRET'),
        #                     aws_access_key_id = os.environ.get('ACCESS'))
         self.data = []
         self.devMode = devMode

    def put(self, data):
        if self.devMode == False:
            self.data.append(data)
        else:
            print(data)

    @withLogging
    def send(self):
        if self.devMode == False:
            response = self.client.put_record(
                StreamName = self.streamName,
                Data = json.dumps(self.data),
                PartitionKey = 'kinesis-stream-key1' # single shard
            )

            return response
        else:
            return None
