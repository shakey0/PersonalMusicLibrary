class Artist:

    def __init__(self, id, name, genre):
        self.id = id
        self.name = name
        self.genre = genre

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Artist({self.id}, {self.name}, {self.genre})"

    def is_valid(self):
        if self.name == None or self.name == "":
            return False
        if self.genre == None or self.genre == "":
            return False
        return True
    
    def generate_errors(self):
        errors = []
        if self.name == None or self.name == "":
            errors.append("Please enter a name for the artist")
        if self.genre == None or self.genre == "":
            errors.append("Please enter a genre for the artist")
        if len(errors) == 0:
            return None
        else:
            return errors
