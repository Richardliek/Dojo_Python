from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask import flash

class Sighting:
    
    db_name = "sasquatch"

    def __init__(self,data):
        self.id = data['id']
        self.location = data['location']
        self.what_happened = data['what_happened']
        self.num_sasquatch = data['num_sasquatch']
        self.date_found = data['date_found']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None

    @classmethod
    def create_sighting(cls, data):
        query = "INSERT INTO sightings (location, what_happened, num_sasquatch, date_found, user_id) VALUES(%(location)s, %(what_happened)s, %(num_sasquatch)s, %(date_found)s, %(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def get_all(cls):
        query= "SELECT * FROM sightings JOIN users ON user_id = users.id;"
        results = connectToMySQL(cls.db_name).query_db(query)
        sightings = []
        row = results[0]
        sighting = cls(row)
        user_data = {
            'id': row['users.id'],
            'first_name': row['first_name'],
            'last_name': row['last_name'],
            'email': row['email'],
            'password': row['password'],
            'created_at': row['users.created_at'],
            'updated_at': row['users.updated_at'],
        }
        user = User(user_data)
        sighting.user = user
        sightings.append(sighting)
        return sightings

## classmethod below does not work to display user names -- would only display one 'sighting' in dashboard

    # @classmethod
    # def get_all(cls):
    #     query= "SELECT * FROM sightings JOIN users ON user_id = users.id;"
    #     results = connectToMySQL(cls.db_name).query_db(query)
    #     sightings = []
    #     for row in results:
    #         sighting = cls(row)
    #         user_data = {
    #             'id': row['users.id'],
    #             'first_name': row['first_name'],
    #             'last_name': row['last_name'],
    #             'email': row['email'],
    #             'password': row['password'],
    #             'created_at': row['users.created_at'],
    #             'updated_at': row['users.updated_at']
    #         }
    #     user = User(user_data)
    #     sightings.user = user
    #     sightings.append(sighting)
    #     Sighting.save(user_data)
    #     return sightings

### END

    @classmethod
    def save(cls,data):
        query = "INSERT INTO sightings (location, what_happened, num_sasquatch, date_found, user_id) VALUES (%(location)s,%(what_happened)s,%(num_sasquatch)s,%(date_found)s,%(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query= "SELECT * FROM sightings JOIN users ON user_id = users.id WHERE sightings.id= %(id)s"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        if len(results) < 1:
            return False
        row = results[0]
        sightings = cls(row)
        user_data = {
            'id': row['users.id'],
            'first_name': row['first_name'],
            'last_name': row['last_name'],
            'email': row['email'],
            'password': row['password'],
            'created_at': row['users.created_at'],
            'updated_at': row['users.updated_at'],
        }
        user = User(user_data)
        sightings.user = user
        return sightings

    @classmethod
    def update(cls, data):
        query = "UPDATE sightings SET location=%(location)s, what_happened=%(what_happened)s, num_sasquatch=%(num_sasquatch)s, date_found=%(date_found)s, updated_at = now() WHERE id= %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def destroy(cls, data):
        query="DELETE FROM sightings WHERE id= %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @staticmethod
    def validate_sightings(sighting):
        isValid = True
        if len(sighting['location']) < 2:
            flash("location must be at least 3 characters","error")
            isValid = False
        if len(sighting['what_happened']) < 2:
            flash("what happened must be at least 3 characters","errror")
            isValid = False
        if len(sighting['date_found']) == "":
            flash("Insert date!","errror")
            isValid = False
        if len(sighting['num_sasquatch']) < 1:
            flash("Insert number of sasquatch","errror")
            isValid = False
        return isValid