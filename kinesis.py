import boto3
import os
import json
from logger import withLogging

class KinesisClient:
    def __init__(self, stream_name):
         self.streamName = stream_name
         self.data = []                 # Keep a buffer to hold data over time
         self.client = boto3.client('kinesis')      # Use IAM role attached to EKS worker nodes

    def put(self, data):
        self.data.append(data)

    @withLogging
    def send(self):
        response = self.client.put_record(
            StreamName = self.streamName,
            Data = json.dumps(self.data),
            PartitionKey = 'kinesis-stream-key1' # single shard
        )
        return response
