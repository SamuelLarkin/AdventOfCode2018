#[1518-04-05 23:59] Guard #1091 begins shift
#[1518-09-09 00:37] falls asleep
#[1518-05-08 00:56] wakes up
#[1518-08-21 00:37] falls asleep
#[1518-10-27 00:05] falls asleep
#[1518-09-25 00:06] falls asleep
#[1518-08-08 00:57] wakes up
#[1518-07-13 00:59] wakes up

import re
from collections import defaultdict
from collections import namedtuple
import numpy as np

Schedule = namedtuple('Schedule', ('schedule', 'max', 'argmax'))
Datum = namedtuple('Datum', (
    'id',
    'schedule',
    'log',
    'total_sleeping_time',
    'longest_nap',
    ))

def read_data(raw_data):
    date_re    = re.compile('\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}\]')
    id_re      = re.compile('\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}\] Guard #(\d+) begins shift')
    asleep_re  = re.compile('\[\d{4}-\d{2}-\d{2} \d{2}:(\d{2})\] falls asleep')
    wake_up_re = re.compile('\[\d{4}-\d{2}-\d{2} \d{2}:(\d{2})\] wakes up')
    guard_id = None
    asleep_time = None
    wakeup_time = None
    raw_data = sorted(map(lambda x: x.strip(), raw_data))
    data = defaultdict(lambda: [])
    for l in raw_data:
        m1 = id_re.match(l)
        m2 = asleep_re.match(l)
        m3 = wake_up_re.match(l)
        if m1:
            guard_id = int(m1.group(1))
            asleep_time = None
            wakeup_time = None
        elif m2:
            assert guard_id is not None
            assert asleep_time is None
            assert wakeup_time is None
            asleep_time = int(m2.group(1))
        elif m3:
            assert guard_id is not None
            assert asleep_time is not None
            assert wakeup_time is None
            wakeup_time = int(m3.group(1))
            data[guard_id].append((asleep_time, wakeup_time))
            asleep_time = None
            wakeup_time = None
        else:
            assert False, l

    full_data = {}
    for guard_id, log_time in data.items():
        #print(guard)
        #print(log_time)
        total_sleeping_time = sum(map(lambda t: t[1]-t[0], log_time))
        longest_nap = max(map(lambda t: t[1]-t[0], log_time))
        #print(total_sleeping_time, longest_nap)
        #data2[guard] = (total_sleeping_time, longest_nap)

        sleep_parttern = np.zeros((60,), dtype=np.int)
        for s, w in log_time:
            mask = np.zeros_like(sleep_parttern)
            mask[s:w] = 1
            sleep_parttern += mask
        #print(sleep_parttern)
        sleepiest_minute = np.argmax(sleep_parttern)

        full_data[guard_id] = Datum(guard_id,
                Schedule(sleep_parttern,
                    np.max(sleep_parttern),
                    np.argmax(sleep_parttern)),
                log_time,
                total_sleeping_time,
                longest_nap)

    return full_data
