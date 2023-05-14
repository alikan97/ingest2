import botocore.session
import botocore
from aws_secretsmanager_caching import SecretCache, SecretCacheConfig

class CachedSecretsManager():
    __instance = None

    def getInstance():
        if CachedSecretsManager.__instance == None:
            CachedSecretsManager()
        return CachedSecretsManager.__instance
    
    def __init__(self) -> None:
        if CachedSecretsManager.__instance != None:
            raise Exception("Singleton class")
        else:
            client = botocore.session.get_session().create_client('secretsmanager')
            cache_config = SecretCacheConfig()
            cache = SecretCache( config = cache_config, client = client)
            CachedSecretsManager.__instance = cache