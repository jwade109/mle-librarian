import os
import logging
from ws_dir import WORKSPACE_DIRECTORY
from datetime import datetime
import hashlib


log = logging.getLogger("resources")
log.setLevel(logging.DEBUG)


# this entire block below is for populating a LOT of resource paths,
# and making it very obvious if (due to negligence, malfeasance, etc)
# the path does not exist, because that's bad
def check_exists(path):
    if not os.path.exists(path):
        print(f"WARNING: required path {path} doesn't exist!")
        log.warning(f"Required path {path} doesn't exist!")
    return os.path.normpath(path)


def ckws(path):
    return check_exists(WORKSPACE_DIRECTORY + path)


GENERATED_FILES_DIR = ckws("/generated")
MLE_YAML = ckws("/persistent/mle.yaml")
MLE_SCRIPTS_DIR = ckws("/mle-scripts")


# returns a unique filename stamped with the current time.
# good for files we want to look at later
def stamped_fn(prefix, ext, dir=GENERATED_FILES_DIR):
    if not os.path.exists(dir):
        os.mkdir(dir)
    return f"{dir}/{prefix}-{datetime.now().strftime('%Y-%m-%dT%H-%M-%S.%f')}.{ext}"


def is_on_windows():
    return os.name == "nt"


def preferred_tmp_dir():
    if is_on_windows():
        return WORKSPACE_DIRECTORY + "/tmp/"
    return "/tmp/bagelbot"


# returns a unique filename in /tmp; for temporary work
# which is not intended to persist past reboots
def tmp_fn(prefix, ext):
    return stamped_fn(prefix, ext, preferred_tmp_dir())


# returns a unique filename in /tmp; for temporary work
# which is not intended to persist past reboots
def hashed_fn(prefix, hashable, ext, dir=preferred_tmp_dir()):
    h = hashlib.md5(hashable).hexdigest()
    if not os.path.exists(dir):
        os.mkdir(dir)
    return f"{dir}/{prefix}-{h}.{ext}"
