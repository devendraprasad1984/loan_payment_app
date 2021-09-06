from solution_using_class_based.utils import enums, utils


class Bank(enums.Enums):
    """store bank entity details"""
    id = None
    name = None
    uid = None


    def __init__(self, id, name):
        """initialize the fields"""
        self.name = name
        self.id = id
        self.uid = utils.Utils(8).get_secret_key()


    def __str__(self):
        return f'bank {self.name}, has id {self.id}'


    def serialize(self):
        return {
            self.key_id: self.id,
            self.key_name: self.name,
            self.key_uid: self.uid
        }


    def get_id(self):
        return self.id


    def get_name(self):
        return self.name


    def get_uid(self):
        return self.uid
