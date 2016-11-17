def chain(func, *args, **kwargs):
    result = None
    if args and kwargs:
        result = func(*args,*kwargs)
    return CallbackAgent(result)

class CallbackAgent:
    def __init__(self, target):
        self.result = target

    def __call__(self, callback):
        result = callback(self.result)
        return CallbackAgent(result)
