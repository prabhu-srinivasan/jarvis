class Task(object):
    """ An interface for defining tasks """
    name = 'Task name':
    description = 'Small description about the task'

    def __init__(**kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def logic(self):
        raise NotImplemented

    def output(self):
        raise NotImplemented
