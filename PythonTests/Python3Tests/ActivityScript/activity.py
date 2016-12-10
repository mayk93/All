import os
import json
import optparse
import subprocess
import datetime
import logging
logging.basicConfig(level=logging.INFO)


def last(path):
    return path.split("/")[len(path.split("/")) - 1]


def up_to_git(path):
    '''

    Go up until the current directory contains "git" in the name

    :param path: A path, most likely the path of the current file
    :return:
    '''

    while not "git" in last(path).lower():
        path = "/".join(path.split("/")[:-1])

    return path


DAY = 60*60*24
try:
    with open("activity.cfg", "r") as config_file:
        config = json.loads(config_file.read())
        BASE_REPO_DIR = config.get("base_repo_dir", up_to_git(os.path.realpath(__file__)))
        SKIP = config.get("to_skip", ["work", ".", "__", "node_modules"])
except FileNotFoundError:
    BASE_REPO_DIR = up_to_git(os.path.realpath(__file__))
    SKIP = ["work", ".", "__", "node_modules"]
logging.info("BASE_REPO_DIR: " + BASE_REPO_DIR)
logging.info("SKIP: " + str(SKIP))



def accepted_depth(original_path, path, allowed_depth=0):
    # logging.info("P len: " + str(len(path.split("/"))))
    # logging.info("OP len: " + str(len(original_path.split("/"))))
    # logging.info("Diff: " + str(len(original_path.split("/")) - len(path.split("/"))))
    # logging.info("Allowing this depth? " + str(len(original_path.split("/")) - len(path.split("/")) > allowed_depth))
    if len(path.split("/")) - len(original_path.split("/")) > allowed_depth:
        return False
    return True


def generate_activity(begin, end, repo_path):
    for root, _, _ in os.walk(repo_path):
        if not accepted_depth(repo_path, root, allowed_depth=1):
            continue
        skipping = False
        for to_skip in SKIP:
            if to_skip.lower() in root.lower():
                skipping = True
                break
        if skipping:
            continue
        if os.path.isdir(root):
            logging.info("Generating activity in: " + root)


def roundTime(dt=None, roundTo=60):
   if dt == None :
       dt = datetime.datetime.now()
   seconds = (dt.replace(tzinfo=None) - dt.min).seconds
   rounding = (seconds+roundTo/2) // roundTo * roundTo
   return dt + datetime.timedelta(0, rounding-seconds, -dt.microsecond)


if __name__ == '__main__':
    parser = optparse.OptionParser()
    # Work on a specific repo
    parser.add_option("-r",
                      "--repo",
                      help="Specify repo for activity",
                      default=None)
    # Begin from
    parser.add_option("-b",
                      "--begin",
                      help="Begin activity from this date. Use -x to specify start x days ago.\n" +
                           "If left empty, will assume today.",
                      default=None)
    # End at
    parser.add_option("-e",
                      "--end",
                      help="End activity at this date. Use -x to specify end x days ago.\n" +
                           "If left empty, will assume today.",
                      default=None)

    (options, _) = parser.parse_args()
    logging.info("Options: " + str(options))

    if options.begin:
        try:
            no_days = int(options.begin[1:])
            begin = roundTime(datetime.datetime.now(), roundTo=DAY) - datetime.timedelta(days=no_days)
        except Exception as e:
            logging.exception(e)
            logging.info("\nDefaulting begin to start of today.\n")
            begin = roundTime(datetime.datetime.now(), roundTo=DAY)
    else:
        begin = roundTime(datetime.datetime.now(), roundTo=DAY)
    if options.end:
        try:
            no_days = int(options.end[1:])
            end = roundTime(datetime.datetime.now(), roundTo=DAY) - \
                  datetime.timedelta(days=no_days) + \
                  datetime.timedelta(hours=23, minutes=59, seconds=59)
        except Exception as e:
            logging.exception(e)
            logging.info("\nDefaulting end to end of today.\n")
            end = roundTime(datetime.datetime.now(), roundTo=DAY) + datetime.timedelta(hours=23, minutes=59, seconds=59)
    else:
        end = roundTime(datetime.datetime.now(), roundTo=DAY) + datetime.timedelta(hours=23, minutes=59, seconds=59)

    if end < begin:
        logging.info("Ending before beginning. Changing around.")
        begin, end = end, begin

    if options.repo:
        repo_path = os.path.join(BASE_REPO_DIR, options.repo)
        logging.info("Working on repo: " + repo_path)
    else:
        repo_path = BASE_REPO_DIR
        logging.info(" -> Working on all repos: " + BASE_REPO_DIR)
    logging.info(" -> Beginning from: " + str(begin))
    logging.info(" -> Ending at: " + str(end))

    generate_activity(begin, end, repo_path)