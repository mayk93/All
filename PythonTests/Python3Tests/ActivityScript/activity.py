import optparse
import subprocess
import datetime


def generate_activity(options):
    pass


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
                      help="Begin activity from this date",
                      default=None)
    # End at
    parser.add_option("-e",
                      "--end",
                      help="End activity at this date",
                      default=None)

    (options, _) = parser.parse_args()

    if options.begin:
        pass
    if options.end:
        pass

    generate_activity(options)