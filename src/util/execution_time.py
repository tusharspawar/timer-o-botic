import time


def execution_time(func):
    def calculate(f):
        execution_start_time = time.time()
        response = func(f)
        response["executionTimeMs"] = "{:.4f}".format((time.time() - execution_start_time) * 1000)
        return response

    return calculate
