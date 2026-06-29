class PersonRecord:
    def __init__(self, id, last_name, first_name, birthdate,  hiredate, lastdate):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.hiredate = hiredate
        self.lastdate = lastdate

    def __repr__(self):
        return (
            f"PersonRecord("
            f"id={self.id}, "
            f"last_name='{self.last_name}', "
            f"first_name='{self.first_name}', "
            f"birthdate={self.birthdate}, "
            f"hiredate={self.hiredate}, "
        )