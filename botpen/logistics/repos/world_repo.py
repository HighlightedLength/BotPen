class WorldRepo:
    size = None
    procedure = None
    time = None
    limit = None

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def set_procedure(self, procedure):
        self.procedure = procedure

    def get_procedure(self):
        return self.procedure

    def set_time(self, time):
        self.time = time

    def get_time(self):
        return self.time

    def set_time_limit(self, limit):
        self.limit = limit

    def get_time_limit(self):
        return self.limit
