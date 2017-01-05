from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import (LoginManager, current_user, login_required,
                            login_user, logout_user, UserMixin, AnonymousUserMixin,
                            confirm_login, fresh_login_required)

import models

class User(UserMixin):
    def __init__(self, email=None, password=None, name=None, active=True, id=None):
        self.email = email
        self.name = name
        self.password = self.set_password_hash(password)
        self.active = active
        self.id = None
        
    def save(self):
        newUser = models.UserSchema(email=self.email, password=self.password, name=self.name, active=self.active)
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
        print(email)
        try:
            dbUser = models.UserSchema.objects.get(email=email)
            
            if dbUser:
                self.email = dbUser.email
                self.active = dbUser.active
                self.name = dbUser.name
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
    
    def email_confirmed(self):
        user = models.UserSchema.objects.get(email=self.email)
        user.email_conf = True
        user.save()
        
    def reset_password(self):
        user = models.UserSchema.objects.get(email=self.email)
        user.password = self.password
        user.save()
        
class Anonymous(AnonymousUserMixin):
    name = u"Anonymous"