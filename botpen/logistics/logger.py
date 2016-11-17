class Logger:
    def debug(self, format, *args):
        if args:
            print(format.format(*args))
        else:
            print(format)
    def info(self, format, *args):
        '''
        if args:
            print(format.format(*args))
        else:
            print(format)
        '''
        pass
    def notice(self, format, *args):
        if args:
            print(format.format(*args))
        else:
            print(format)

    def warn(self, format, *args):
        if args:
            print(format.format(*args))
        else:
            print(format)

    def error(self, format, *args):
        if args:
            print(format.format(*args))
        else:
            print(format)

    def critical(self, format, *args):
        if args:
            print(format.format(*args))
        else:
            print(format)

    def alert(self, format, *args):
        if args:
            print(format.format(*args))
        else:
            print(format)

    def emergency(self, format, *args):
        if args:
            print(format.format(*args))
        else:
            print(format)
