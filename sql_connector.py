import mysql.connector
import config
from flask import jsonify


connection_params = {
        'host' : config.host_db,
        'user': config.user_db,
        'password' : config.password_db,
        'database' : config.database,
        'port' : config.port_db,
    }


def get_user_info(id):
    try:
        params = []
        requete = "SELECT username, nom, prenom, email, date_creation FROM utilisateur WHERE id=%s"
        params.append(id)
        with mysql.connector.connect(**connection_params) as db :
            with db.cursor() as c:
                c.execute(requete, params)
                results =  c.fetchall()
        pretty_results = {}
        if results:
            pretty_results['username'] = results[0][0]
            pretty_results['nom'] = results[0][1]
            pretty_results['prenom'] = results[0][2]
            pretty_results['email'] = results[0][3]
            pretty_results['date_creation'] = results[0][4]
        else: 
            pretty_results['error'] = "Utilisateur non trouvé"
        return pretty_results
    except Exception as err:
        return  'error : mysql_connector. Error : ' + str(err)

def get_user_id(username):
    try:
        params = []
        requete = "SELECT id FROM utilisateur WHERE username=%s"
        params.append(username)
        with mysql.connector.connect(**connection_params) as db :
            with db.cursor() as c:
                c.execute(requete, params)
                results =  c.fetchall()
        pretty_results = {}
        if results:
            pretty_results['id'] = results[0][0]
        else: 
            pretty_results['error'] = "Utilisateur non trouvé"
            pretty_results['id'] = None
        return pretty_results
    except Exception as err:
        return  'error : mysql_connector. Error : ' + str(err)