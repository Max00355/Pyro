from flask import Flask, session, redirect
from index import index
from login import login
from register import register
import os

app = Flask(__name__)
app.secret_key = "B0`nIly0!_A!Hx9WE%CdSDZ`}DoJ#r09#w(_pCKY%wPM=@)kS GkE!%B@Tq=Z-kQ" #Do not share this with anyone.
app.debug = True


app.register_blueprint(index)
app.register_blueprint(register)
app.register_blueprint(login)

@app.route("/logout/")
def logout():
    session.pop("login")
    return redirect("/")

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))

	if port == 5001:		
		app.run('0.0.0.0', port=port)
