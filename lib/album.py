class Album():

    def __init__(self, id, title, release_year, artist_id):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Album({self.id}, {self.title}, {self.release_year}, {self.artist_id})"
    
    def is_valid(self):
        if self.title == None or self.title == "":
            return False
        if not isinstance(self.release_year, int) or self.release_year < 1930 or self.release_year > 2023:
            return False
        if not isinstance(self.artist_id, int) or self.artist_id < 1:
            return False
        return True
    
    def generate_errors(self):
        errors = []
        if self.title == None or self.title == "":
            errors.append("Please enter an album title")
        if not isinstance(self.release_year, int) or self.release_year < 1930 or self.release_year > 2023:
            errors.append("Please select a year")
        if not isinstance(self.artist_id, int) or self.artist_id < 1:
            errors.append("Please select an artist")
        if len(errors) == 0:
            return None
        else:
            return errors