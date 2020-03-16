import os
from server.instance import server

env_name = os.environ['env'] or 'dev'

if __name__ == '__main__':
    server.run(env_name)
