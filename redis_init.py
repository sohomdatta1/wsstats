import os
import redis

redis_url = 'redis://localhost:6379/9'

if 'NOTDEV' in os.environ:
    redis_url = 'redis://redis.svc.tools.eqiad1.wikimedia.cloud:6379/0'


REDIS_KEY_PREFIX = 'mw-toolforge-wsstats'