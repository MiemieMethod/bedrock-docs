from functools import wraps

import time
import uuid


class TimerManager(object):

    global_timer = {}
    global_timer_duration = {}

    @classmethod
    def __start(cls, duration, repeat, func, *args, **kwargs):
        is_done = False
        start_time = time.time() * 1000000
        while True:
            state = cls.__wait_for_seconds(start_time, duration)
            is_done = state.next()
            yield is_done
            if is_done is True:
                cancel = func(*args, **kwargs)
                if repeat is False or cancel is True:
                    break
                start_time = time.time() * 1000000
                is_done = False

    @classmethod
    def __wait_for_seconds(cls, start_time, duration):
        while True:
            end_time = time.time() * 1000000 - start_time
            if end_time >= duration * 1000000:
                yield True
            else:
                yield end_time

    @classmethod
    def start_timer(cls, duration, repeat):
        def decorate(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                task_id = uuid.uuid4()
                cls.global_timer[task_id] = cls.__start(
                    duration, repeat, func, *args, **kwargs)
                return task_id
            return wrapper
        return decorate

    @classmethod
    def stop_timer(cls, task_id):
        if task_id in cls.global_timer:
            del cls.global_timer[task_id]
        if task_id in cls.global_timer_duration:
            del cls.global_timer_duration[task_id]

    @classmethod
    def is_timer_finish(cls, task_id):
        return True if task_id not in cls.global_timer else False

    @classmethod
    def update(cls):
        for key in cls.global_timer.keys():
            try:
                generator_value = cls.global_timer.get(key, '')
                if generator_value:
                    end_time = cls.global_timer[key].next()
                    cls.global_timer_duration[key] = end_time
            except StopIteration:
                cls.stop_timer(key)
