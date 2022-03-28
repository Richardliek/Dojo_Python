from flask_app.models.user import User
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Thought:
    
    db_name = 'thoughts_schema'

    def __init__(self,db_data):
        self.id = db_data['id']
        self.thought = db_data['thought']
        self.likes = db_data['likes']
        self.user_id = db_data['user_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.user = None

    @classmethod
    def add_thought(cls, data):
        query = "INSERT INTO thoughts(thought, user_id) VALUES(%(thought)s, %(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM thoughts;"
    #     results = connectToMySQL(cls.db_name).query_db(query)
    #     all_thoughts = []
    #     for row in results:
    #         thought = cls(row)
    #         user_data = {
    #             'id' : row['user.id'],
    #             'first_name' : row['first_name'],
    #             'last_name' : row['last_name'],
    #             'email' : row['email'],
    #             'password' : row['password'],
    #             'created_at' : row['created_at'],
    #             'updated_at' : row['updated_at']
    #         }
    #         user = User(user_data)
    #         all_thoughts.append(thought)
        # return all_thoughts

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM thought;"
        results = connectToMySQL(cls.db_name).query_db(query)
        thoughts = []
        for row in results:
            thoughts.append(cls(row))
        return thoughts


    # @classmethod
    # def save(cls,data):
    #     query = "INSERT INTO thought (thoughts, user_id) VALUES (%(thoughts)s,%(user_id)s);"
    #     return connectToMySQL(cls.db_name).query_db(query, data)

    
    # @classmethod
    # def destroy(cls,data):
    #     query = "DELETE FROM pie WHERE id = %(id)s;"
    #     return connectToMySQL(cls.db_name).query_db(query,data)

    # @staticmethod
    # def validate_thoughts(thought):
    #     is_valid = True
    #     if len(thought['name']) < 3:
    #         is_valid = False
    #         flash("Name must be at least 3 characters","thought")
    #     if len(recipe['instructions']) < 3:
    #         is_valid = False
    #         flash("Instructions must be at least 3 characters","recipe")
    #     if len(recipe['description']) < 3:
    #         is_valid = False
    #         flash("Description must be at least 3 characters","recipe")
    #     if recipe['date_made'] == "":
    #         is_valid = False
    #         flash("Please enter a date","recipe")
    #     return is_valid
