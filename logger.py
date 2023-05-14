import requests
import json
import datetime
from secretmanager import CachedSecretsManager

cachedSecretsClient = CachedSecretsManager()
Splunk_credentials = json.loads(cachedSecretsClient.getInstance().get_secret_string('dev/splunk'))

HOST = "http://" + Splunk_credentials['SPLUNK_HOST']
API_KEY = Splunk_credentials['SPLUNK_API_KEY']
PORT = Splunk_credentials['SPLUNK_PORT']
LOG_URI = "/services/collector/event"

class Log_Level():
    SUCCESS = 'SUCCESS'
    DEBUG = 'DEBUG'
    WARN = 'WARN'
    ERROR = 'ERROR'

def withLogging(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            send_log(Log_Level.SUCCESS, f'sent records to Kinesis: {result["SequenceNumber"]}')

            if hasattr(result, 'FailedRecordCount'):
                send_log(Log_Level.WARN, f'Missed {result.FailedRecordCount} records when sending to kinesis')

            return result
        except Exception as e:
            send_log(Log_Level.ERROR, f'Error occurred: {e}')
            
    return wrapper

def send_log(level: Log_Level, message):
    event = {
        'sourcetype': 'json',
        'level': level,
        'event': message
    }

    response = requests.post(HOST+":"+PORT+LOG_URI,
                            headers={"Authorization": f'Splunk {API_KEY}'},
                            data=json.dumps(event, ensure_ascii=False).encode('utf-8'))
