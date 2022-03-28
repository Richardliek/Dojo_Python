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
        for row in results:
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

    ## Initiating favorites (likes) ##

    # @classmethod
    # def get_all_with_favorites(cls):
    #     query= "SELECT * FROM sasquatch JOIN users ON users.id=opinions.user_id "\
    #             "LEFT JOIN skeptics ON opinions.id = skeptics.opinion_id "\
    #             "LEFT JOIN users AS users2 ON users2.id = skeptics.user_id "\
    #             "ORDER BY sasquatch.created_at DESC; "\

    #     results = connectToMySQL(cls.db).query_db(query)
    #     opinions = [] 
    #     for result in results:
    #         new_opinion = True
    #         like_user_data = {
    #             "id" : result["users2.id"],
    #             "first_name": result["users2.first_name"],
    #             "last_name": result["users2.last_name"],
    #             "email": result["users2.email"],
    #             "password": result["users2.password"],
    #             "created_at": result["users2.created_at"],
    #             "updated_at": result["users2.updated_at"]
    #         }
    #         # opinions have been added, and the last one added is the same opinion as the current row(multiple users who liked)
    #         if len(opinions) > 0 and opinions[len(opinions)-1].id == result['id']:
    #             opinions[len(opinions)-1].users_who_favorited.append(User(like_user_data))
    #             new_opinion = False

    #         if new_opinion:
    #             opinion = cls(result)

    #             #Put all relevant user information into a new data dictionary
    #             user_data = {
    #                 'id': result['users.id'],
    #                 'first_name': result['first_name'],
    #                 'last_name': result['last_name'],
    #                 'email': result['email'],
    #                 'password': result['password'],
    #                 'created_at': result['users.created_at'],
    #                 'updated_at': result['users.updated_at'],
    #             }
    #             #Create a user object with the user data
    #             user = User(user_data)


    #             # Set user attribute in opinion object to the newly created user object
    #             opinion.user = user

    #             # if there is a user who liked, then add it to the list
    #             if result['users2.id'] is not None:
    #                 opinion.users_who_favorited.append(User(like_user_data))
    #             opinions.append(opinion)
    #     return opinions

    # @classmethod
    # def get_all_user_favorited_opinions(cls, data):
    #     opinions_liked = []
    #     query="SELECT opinion_id FROM favorited_opinions JOIN users ON users.id=user_id WHERE user_id=%(id)s"
    #     results = connectToMySQL(cls.db).query_db(query, data)
    #     for result in results:
    #         opinions_liked.append(result['opinion_id'])
    #     return opinions_liked

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

    ##Like and dislike buttons##
    
    @classmethod
    def like(cls, data):
        query="INSERT INTO favorited_opinions(user_id, opinion_id) VALUES(%(user_id)s,%(opinion_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)
    @classmethod
    def dislike(cls, data):
        query="DELETE FROM favorited_opinions WHERE opinion_id=%(opinion_id)s AND user_id=%(user_id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

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