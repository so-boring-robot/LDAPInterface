from django.shortcuts import render
from ldap3 import Server, Connection, ALL
from django.conf import settings


def connect_to_ldap():
    server = Server(settings.LDAP_URI, get_info=ALL)
    conn = Connection(server, user=settings.BIND_DN, password=settings.BIND_PASSWORD)
    if not conn.bind():
        print("Erreur de connexion :", conn.result)
        return False 
    print("✅ Connecté au serveur LDAP")
    return conn

###
# TO CHANGE - For now, it only shows sudoer users
###
def list_users(): 
    conn = connect_to_ldap()
    conn.search(
      search_base= "cn=sudoers,"+settings.BASE_DN,
      search_filter="(uid=*)",
      attributes=["cn", "sn", "uid", "mail"]
    )
    # Parcours des résultats
    print("Début Liste : ")
    for entry in conn.entries:
      print(f"UID: {entry.uid}, Nom: {entry.cn}, Email: {entry.mail}")
    conn.unbind()