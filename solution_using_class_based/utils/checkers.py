class Checker():
    """some utils checker functions"""


    def check_present_of_same_name_object(self, object=None, name=None):
        if object == None or name == None: return False

        found = False
        for b in object:
            if b.get_name() == name:
                found = True
                break
        return found
