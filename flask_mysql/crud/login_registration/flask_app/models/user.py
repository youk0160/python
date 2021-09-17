# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.pwd = data['pwd']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users_schema').query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
        return users
    
    @classmethod
    def save(cls, data):
        query="insert into users (first_name, last_name, email, pwd, created_at, updated_at) values (%(first_name)s, %(last_name)s, %(email)s, %(pwd)s, Now(), Now())"
        return connectToMySQL('users_schema').query_db(query, data)
    
    @staticmethod
    def validate_user(user):
        is_valid = True # we assume this is true
        users = User.get_all()
        for x in users:
            if(x.email == user['email']):
                flash("Email already exists in the database", "register")
                is_valid = False
        if not re.match("^[a-zA-Z]{2,}$",user['first_name']):
            flash("First name must be at least 2 characters and contain only alphabets.", "register")
            is_valid = False
        if not re.match("^[a-zA-Z]{2,}$",user['last_name']):
            flash("Last name must be at least 2 characters and contain only alphabets.", "register")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", "register")
            is_valid = False
        if len(user['pwd']) < 8:
            flash("Pwd must be at least 3 characters.", "register")
            is_valid = False
        if user['conf_pwd'] != user['pwd']:
            flash("Passwords don't match", "register")
            is_valid = False
        return is_valid
    
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("users_schema").query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])