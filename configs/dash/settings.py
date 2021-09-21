import socket
from configs.secrets import DEV_HOSTS_NAMES


HOST = "0.0.0.0"
PORT = 80
THREADED = True

PROJECT_NAME = "G3-Simulator"
PY_FILE_EXTENSION = ".py"

TESTS_COMMAND_LINE = "python -m unittest"
RUN_TESTS = socket.gethostname() in DEV_HOSTS_NAMES


