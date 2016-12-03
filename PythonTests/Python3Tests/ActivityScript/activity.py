import optparse
import subprocess
import datetime
import logging


DAY = 60*60*24


def generate_activity(repo=None):
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
    print("Options: ", options)

    if options.begin:
        try:
            no_days = int(options.begin[1:])
            begin = roundTime(datetime.datetime.now(), roundTo=DAY) - datetime.timedelta(days=no_days)
        except:
            logging.exception(e)
            begin = roundTime(datetime.datetime.now(), roundTo=)
    else:
        pass
    if options.end:
        try:
            pass
        except AssertionError:
            pass
    else:
        pass

    generate_activity(repo=options.repo)