# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id=data['dojo_id']
    # Now we use class methods to query our database
    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM dojos;"
    #     # make sure to call the connectToMySQL function with the schema you are targeting.
    #     results = connectToMySQL('dojo_ninjas').query_db(query)
    #     # Create an empty list to append our instances of friends
    #     dojos = []
    #     # Iterate over the db results and create instances of friends with cls.
    #     for dojo in results:
    #         dojos.append( cls(dojo) )
    #     return dojos
    
    @classmethod
    def save(cls, data):
        query="insert into ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) values (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, Now(), Now())"
        return connectToMySQL('dojo_ninjas').query_db(query, data)