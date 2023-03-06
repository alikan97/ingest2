import boto3
import os
import json
class KinesisClient:
    def __init__(self, stream_name):
         self.streamName = stream_name
         self.client = boto3.client('kinesis',
                            region_name = os.environ.get('REGION'),
                            aws_secret_access_key = os.environ.get('SECRET'),
                            aws_access_key_id = os.environ.get('ACCESS'))
         self.data = []

    def put(self, data, partition_key):
        self.data.append(data)

    def send(self):

        response = self.client.put_record(
             StreamName = self.streamName,
             Data = json.dumps(self.data),
             PartitionKey = 'kinesis-stream-key1' # single shard
        )

        if response.FailedRecordCount != 0:
            print('Error occurred') # send to splunk
        
        withLogging(Type="Success", Message="Sent {0} records to kinesis") # Something like this

def withLogging():
    # Implement function decorator for splunk logging
    return 0
