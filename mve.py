import argparse
import json
import os
import pathlib
import subprocess
import sys

CONFIGS_KEY: str = 'MVE_CONFIGS'
CONFIG_BASENAME: str = 'config.json'


def main():

    configs_path: str = os.environ.get(CONFIGS_KEY, None)
    if configs_path is None:
        print(
            f'the environment variable ${CONFIGS_KEY} has not been set', file=sys.stderr)
        sys.exit(1)

    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('config', type=str)
    args: argparse.Namespace = parser.parse_args()

    config: str = args.config

    config_file: str = os.path.join(configs_path, config, CONFIG_BASENAME)
    try:
        with open(config_file, 'r') as c:
            cfg: dict = json.load(c)
    except FileNotFoundError:
        print(
            f'the config file ${config_file.replace(configs_path, CONFIGS_KEY)} does not exist', file=sys.stderr)
        sys.exit(2)

    set_host_docker_path_pair(cfg, 'SOURCE')
    set_host_docker_path_pair(cfg, 'RENAMES')
    set_host_docker_path_pair(cfg, 'DESTINATION')

    configs_docker: str = pathlib.PurePosixPath(
        *os.path.split(configs_path)).as_posix()

    os.environ[CONFIGS_KEY] = configs_docker

    # subprocess.run(['docker-compose', 'up', '--build'])


def set_host_docker_path_pair(cfg: dict, key: str):
    paths_list: list[str] = cfg[key]
    os.environ[f'{key}_HOST'] = os.path.join(*paths_list)
    os.environ[f'{key}_DOCKER'] = pathlib.PurePosixPath(*paths_list).as_posix()


if __name__ == '__main__':
    main()
