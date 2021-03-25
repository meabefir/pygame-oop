class Events:
    events = {}

    @staticmethod
    def connect(event, obj, callback):
        if event in Events.events:
            Events.events[event].append((obj, callback))
        else:
            Events.events[event] = [(obj, callback)]

    @staticmethod
    def disconnect(event, obj, callback):
        if (obj, callback) in Events.events[event]:
            Events.events[event].remove((obj,callback))

    @staticmethod
    def emit(signal, *args):
        if signal in Events.events:
            for connection in Events.events[signal]:
                obj, callback = connection
                callback(*args)
