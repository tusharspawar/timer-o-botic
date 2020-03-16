import argparse
from server.instance import server
from util.util import validate_env_name

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Read application environment')
    parser.add_argument('--env',
                        dest='env',
                        default='dev',
                        type=validate_env_name,
                        help='Valid environment values: dev, stg and prod. Default is dev.')

    args = parser.parse_args()
    env_name = args.env
    server.run(env_name)
