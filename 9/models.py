class Model:

    def __iter__(self):
        return (item for item in self.__class__.__dict__ if not item.startswith('__'))

    def __getitem__(self, key):
        return getattr(self, key)

    def __len__(self):
        return len(list(self.__iter__()))


class CharField:

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def query(self):
        return 'VARCHAR({}) {} {}'.format(
                    self.max_length,
                    "UNIQUE KEY" if hasattr(self, 'unique') and getattr(self, 'unique') == True else '', 
                    "PRIMARY KEY" if hasattr(self, 'primary_key') and getattr(self, 'primary_key') == True  else '', 
                    )


class IntField:

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def query(self):
        return 'INT {} {}'.format(
                    "AUTO_INCREMENT" if hasattr(self, 'autoincrement') and getattr(self, 'autoincrement') == True else '', 
                    "PRIMARY KEY" if hasattr(self, 'primary_key') and getattr(self, 'primary_key') == True  else '', 
                    )
