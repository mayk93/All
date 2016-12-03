import optparse
import subprocess
import datetime
import logging
logging.basicConfig(level=logging.INFO)


DAY = 60*60*24


def generate_activity(begin, end, repo=None):
    pass


def roundTime(dt=None, roundTo=60):
   """Round a datetime object to any time laps in seconds
   dt : datetime.datetime object, default now.
   roundTo : Closest number of seconds to round to, default 1 minute.
   Author: Thierry Husson 2012 - Use it as you want but don't blame me.
   """
   if dt == None : dt = datetime.datetime.now()
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
        logging.info("Working on repo: ", options.repo)
    else:
        logging.info("Working on all repos.")
    logging.info("Beginning from: " + str(begin))
    logging.info("Ending at: " + str(end))

    generate_activity(begin, end, repo=options.repo)