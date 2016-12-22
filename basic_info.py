class Basic_Info(object):
    """docstring for Module"""
    def __init__(self, **kwargs):
        self.first_name = input('First name: ')
        self.last_name = input('Last name: ')
        self.title = input('Title: ')
        self.phone = input('Phone number: ')
        self.address = input('Address: ')
        self.dept = input('Department: ')
        self.notes = input('Notes: ')

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return "\nname:{} {},\ntitle: {}".format(self.first_name, self.last_name, self.title,)

