# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

# model the class after the friend table from our database
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas=[]
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojo_ninjas').query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos
    
    @classmethod
    def find_dojo(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(dojo_id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojo_ninjas').query_db(query, data)

        dojo = cls( results[0] )

        print(results)

        for row_in_db in results:
            ninja_data = {
                'id' : row_in_db['ninjas.id'],
                'first_name' : row_in_db['first_name'],
                'last_name' : row_in_db['last_name'],
                'age' : row_in_db['age'],
                'created_at' : row_in_db['ninjas.created_at'],
                'updated_at' : row_in_db['ninjas.updated_at'],
                'dojo_id' : row_in_db['dojo_id']
            }
            dojo.ninjas.append( ninja.Ninja(ninja_data) )

        return dojo

    @classmethod
    def save(cls, data):
        query="insert into dojos (name, created_at, updated_at) values (%(name)s, Now(), Now())"
        return connectToMySQL('dojo_ninjas').query_db(query, data)