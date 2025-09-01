# 📂 LDAPInterface

**LDAPInterface** est une application web de gestion d’annuaire **OpenLDAP**, développée avec **Django**, du HTML/CSS et du JavaScript vanilla.  
Elle offre une interface moderne et intuitive pour administrer facilement les utilisateurs et unités d’organisation.

---

## ✨ Fonctionnalités

- **Gestion des comptes** : activation / désactivation / suppression / modification.
- **Liste des utilisateurs** avec :
  - Nom, prénom
  - UID
  - Email
  - Rôles
  - Statut actif/inactif
  - Date d’ajout
- **Ajout d’un utilisateur** via formulaire.
- **Import en masse** d’utilisateurs via fichier CSV.
- **Filtres et recherche** :
  - Par statut (actif/inactif)
  - Par unité d’organisation (OU)
  - Recherche par nom, prénom, UID, email
- **Tri et pagination**.
- **Interface responsive** adaptée aux mobiles et tablettes.

---

## 🛠️ Technologies utilisées

- **Backend** : [Django](https://www.djangoproject.com/) (Python)
- **Frontend** : HTML5, CSS3, JavaScript vanilla
- **LDAP** : OpenLDAP (via `ldap3`)
- **Base de données** : MySQL
- **Gestion des styles** : CSS pur
- **Outils** : Django Templates

---

## 📦 Installation

### 1️⃣ Cloner le dépôt
```bash
git clone https://github.com/ton-compte/LDAPInterface.git
cd LDAPInterface
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
pip install -r requirements.txt

NB : I'm not an UX Designer...So the frontend is made by Copilot. Thanks AI <3