import argparse
import os
import subprocess
import sys


#: The name of the environment variable that would contain `/path/to/google-java-format-1.3-all-deps.jar`
JAVA_FORMAT_JAR_ENV_NAME = 'GOOGLE_JAVA_FORMAT_JAR'


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    filenames = args.filenames

    jar_location = os.environ.get(JAVA_FORMAT_JAR_ENV_NAME)
    if not jar_location:
        print("Unable to locate location of the google-java-format jar")
        return 0

    if not filenames:
        print("No filenames were changed, skipping this hook")
        return 0

    command = [
        "java",
        "-jar",
        jar_location,
    ]
    command += filenames

    proc = subprocess.Popen(
        command,
        stdout=None,
        stderr=None,
    )
    proc.wait()
    return proc.returncode
