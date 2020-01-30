
# https://www.codewars.com/kata/human-readable-time/python

def make_readable(seconds):
    minutes = seconds // 60
    rem_seconds = seconds - (minutes * 60)
    hours = (minutes // 60)
    rem_minutes = minutes - (hours * 60)
    return '{0:02d}:{1:02d}:{2:02d}'.format(hours, rem_minutes, rem_seconds)


# def make_readable(s):
#     return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)
