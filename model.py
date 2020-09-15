import sqlite3 as sql

from functools import wraps
from flask import session, flash, redirect, url_for

connect_db = 'msl.db'
    
    
def checklogin(id_user,password):
    with sql.connect(connect_db) as db:
        qry = 'select id_user,password from user where id_user=? and password=?'
        result=db.execute(qry,(id_user,password)).fetchone()
        return(result)    
    
#end login
#helper function
def login_required(f):
    @wraps(f)
    def wrap (*args,**kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for('home'))
    return wrap
 