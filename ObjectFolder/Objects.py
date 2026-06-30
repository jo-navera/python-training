class PersonRecord:
    def __init__(self, id, last_name, first_name, birthdate, role, hiredate, lastdate):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.role = role
        self.hiredate = hiredate
        self.lastdate = lastdate

    def __repr__(self):
        return (
            f"PersonRecord("
            f"id={self.id}, "
            f"last_name='{self.last_name}', "
            f"first_name='{self.first_name}', "
            f"birthdate={self.birthdate}, "
            f"role={self.role}, "
            f"hiredate={self.hiredate}, "
            f"lastdate={self.lastdate}, "
        )