from flask_app.controllers import dojo_controller
from flask_app.controllers import ninja_controller
from flask_app import app

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
