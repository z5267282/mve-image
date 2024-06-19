import argparse
import json
import os
import pathlib
import subprocess
import sys

CONFIGS_KEY: str = 'MVE_CONFIGS'
CONFIG_BASENAME: str = 'config.json'

SOURCE_CONFIG_KEY = 'SOURCE'
RENAMES_CONFIG_KEY = 'RENAMES'
DESTINATION_CONFIG_KEY = 'DESTINATION'


def main():
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('config', type=str)
    args: argparse.Namespace = parser.parse_args()
    config: str = args.config

    configs_path: str = os.environ.get(CONFIGS_KEY, None)
    if configs_path is None:
        print(
            f'the environment variable ${CONFIGS_KEY} has not been set', file=sys.stderr)
        sys.exit(1)

    config_file: str = os.path.join(configs_path, config, CONFIG_BASENAME)
    try:
        with open(config_file, 'r') as c:
            cfg: dict = json.load(c)
    except FileNotFoundError:
        print(
            f'the config file ${config_file.replace(configs_path, CONFIGS_KEY)} does not exist', file=sys.stderr)
        sys.exit(2)

    set_host_docker_path_pair(cfg, SOURCE_CONFIG_KEY)
    set_host_docker_path_pair(cfg, RENAMES_CONFIG_KEY)
    set_host_docker_path_pair(cfg, DESTINATION_CONFIG_KEY)

    configs_docker: str = pathlib.PurePosixPath(
        *os.path.split(configs_path)).as_posix()

    os.environ[CONFIGS_KEY] = configs_docker

    # subprocess.run(['docker-compose', 'up', '--build'])


def set_host_docker_path_pair(cfg: dict, key: str):
    paths_list: list[str] = cfg[key]
    host, docker = create_abs_docker_path_pair(paths_list)
    os.environ[f'{key}_HOST'] = host
    os.environ[f'{key}_DOCKER'] = docker


def create_abs_docker_path_pair(paths: list[str]) -> tuple[str, str]:
    return os.path.join(*paths), pathlib.PurePosixPath(*paths).as_posix()


if __name__ == '__main__':
    main()
