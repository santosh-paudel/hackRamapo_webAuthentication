from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import (LoginManager, current_user, login_required,
                            login_user, logout_user, UserMixin, AnonymousUserMixin,
                            confirm_login, fresh_login_required)

import models

class User(UserMixin):
    def __init__(self, email=None, password=None, active=True, id=None):
        self.email = email
        self.password = self.set_password_hash(password)
        self.active = active
        self.id = None
        
    def save(self):
        newUser = models.UserSchema(email=self.email, password=self.password, active=self.active)
        newUser.save()
        print("New userID: " + str(newUser.id))
        self.id = newUser.id
        return self.id
    
    def set_password_hash(self, password):
        if password != None:
            return generate_password_hash(password)
        return None
    
    def check_password(self, password): 
        return check_password_hash(self.password, password)
    
    def get_user_with_email(self, email):
        try:
            dbUser = models.UserSchema.objects.get(email=email)
            
            if dbUser:
                self.email = dbUser.email
                self.active = dbUser.active
                self.password = dbUser.password
                self.id = dbUser.id
                return self
            else:
                return None
        except:
            print ("An error occurred")
            return None
    
    def get_user_id(self, id):
        dbUser = models.UserSchema.objects.with_id(id)
        if dbUser:
            self.email = dbUser.email
            self.active = dbUser.active
            self.id = dbUser.id
            return self
        else:
            return None    
        
class Anonymous(AnonymousUserMixin):
    name = u"Anonymous"