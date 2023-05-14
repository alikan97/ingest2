import requests
import json
import datetime
from secretmanager import CachedSecretsManager

cachedSecretsClient = CachedSecretsManager()

HOST = cachedSecretsClient.getInstance().get_secret_string('SPLUNK_HOST')
API_KEY = cachedSecretsClient.getInstance().get_secret_string('SPLUNK_API_KEY')
PORT = cachedSecretsClient.getInstance().get_secret_string('SPLUNK_PORT')
LOG_URI = "/services/collector/event"

class Log_Level():
    SUCCESS = 1
    DEBUG = 2
    WARN = 3
    ERROR = 4

def withLogging(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            send_log(Log_Level.SUCCESS, f'{func.__name__} sent following records to Kinesis: {result}', True)

            if result.FailedRecordCount != 0:
                send_log(Log_Level.WARN, f'{func.__name__} Missed {result.FailedRecordCount} records when sending to kinesis', True)

            return result
        except Exception as e:
            send_log(Log_Level.ERROR, f'Error occurred: {e}', True)
            
    return wrapper

def send_log(level: Log_Level, message):
    event = {
        'timestamp': datetime.datetime.now(),
        'level': level,
        'message': message
    }

    response = requests.post(HOST+LOG_URI,
                            headers={"Authorization": f'Splunk {API_KEY}'},
                            data=json.dumps(event, ensure_ascii=False).encode('utf-8'))
    
    return response
