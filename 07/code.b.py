#!/usr/bin/env python

from __future__ import print_function

from collections import namedtuple
from collections import defaultdict
from utils import test_data
from utils import parse_dependencies
from utils import complete_graph
import logging


RunningTask = namedtuple('RunningTask', ('name', 'time'))





if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        deps = parse_dependencies(f)
        alphabet = set(map(chr, range(ord('A'), ord('Z')+1)))

    debug = False
    if debug:
        deps = parse_dependencies(test_data)
        alphabet = set(map(chr, range(ord('A'), ord('F')+1)))

    tasks = defaultdict(lambda: set())
    for p, c in deps:
        tasks[c].add(p)
    tasks = complete_graph(tasks)
    logging.getLogger(__name__).debug('tasks: {}'.format(tasks))

    running_tasks = []
    total_time = 0
    while tasks or running_tasks:
        # A task is available next if it is not currently been done and when all its dependencies have been met.
        available_tasks = [ task for task, deps in tasks.items() if not deps and task not in (name for name, time in running_tasks) ]
        logging.getLogger(__name__).debug('available_tasks: {}'.format(available_tasks))
        if available_tasks and len(running_tasks) < 5:
            next_task = min(available_tasks)  # tasks are added in alphabetical order amongst the available tasks.
            new_task = RunningTask(next_task, 60 + ord(next_task) - ord('A') + 1)
            running_tasks.append(new_task)
            logging.getLogger(__name__).debug('Adding: {}'.format(new_task))
        else:
            # what is the next task to finish
            next_task_to_finish = min(running_tasks, key=lambda t: t.time)
            logging.getLogger(__name__).debug('Done: {}'.format(next_task_to_finish))
            # Add how long that task took to finish
            total_time += next_task_to_finish.time
            # Calculate the remaining run time for current tasks in progress.
            running_tasks = map(lambda t: RunningTask(t.name, t.time - next_task_to_finish.time), running_tasks)
            # Remove the finish task.
            running_tasks = list(filter(lambda t: t.time > 0, running_tasks))
            # Remove the currently finish task from other task dependencies
            # which will allow them to potentially run next.
            for t, d in tasks.items():
                d.discard(next_task_to_finish.name)
            # Remove the finished task from the task list.
            del(tasks[next_task_to_finish.name])
            logging.getLogger(__name__).debug('tasks: {}'.format(tasks))

    print('Answer:', total_time)
    # 1234
