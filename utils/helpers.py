import isodate

def parse_duration(duration):
    return isodate.parse_duration(duration).total_seconds()