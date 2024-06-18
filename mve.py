import json
import os
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

# TODO: read source
# TODO: read destination
# TODO: read edits

# TODO: create os specific path via os.path.join
# TODO: create linux pure path via Pathlib

# TODO: convert MVE_CONFIGS to pure posix path, then export this to child

# subprocess.run(["docker-compose", "up", "--build"])
