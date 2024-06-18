import json
import os
import pathlib
import subprocess
import sys

CONFIGS_KEY: str = "MVE_CONFIGS"

CONFIG_BASENAME: str = "config.json"

configs_path: str = os.environ.get(CONFIGS_KEY, None)
if configs_path is None:
    print(
        f"the environment variable {CONFIGS_KEY} has not been set", file=sys.stderr)
    sys.exit(1)

config, = sys.argv[1:]

config_file = os.path.join(configs_path, config, CONFIG_BASENAME)
try:
    with open(config_file, "r") as c:
        cfg: dict = json.load(c)
except FileNotFoundError:
    print(
        f"the config file {config_file.replace(configs_path, CONFIGS_KEY)} does not exist", file=sys.stderr)
    sys.exit(2)


def create_abs_docker_path_pair(paths: list[str]) -> tuple[str, str]:
    return os.path.join(*paths), pathlib.PurePosixPath(*paths)


source: list[str] = cfg["SOURCE"]
source_abs, source_docker = create_abs_docker_path_pair(source)

renames: list[str] = cfg["RENAMES"]
renames_abs, renames_docker = create_abs_docker_path_pair(renames)

edits: list[str] = cfg["DESTINATION"]
edits_abs, edits_docker = create_abs_docker_path_pair(edits)

configs_docker: str = os.path.join(
    *pathlib.PurePosixPath(
        *os.path.split(configs_path)
    ).parts
)

os.environ[CONFIGS_KEY] = configs_docker

# subprocess.run(["docker-compose", "up", "--build"])
