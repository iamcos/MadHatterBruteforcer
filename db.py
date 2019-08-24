from tinydb import TinyDB, Query
db = TinyDB('db.json')

Group = Query()
Permission = Query()
groups = db.table('groups')
groups.insert({'user':' me', 'permissions': [{'type': 'read'},{'type' : 'sudo'}]})
groups.insert({'user':' you', 'permissions': [{'type': 'write'},{'type' : 'sudo'}]})

d = groups.search(Group.permissions.any(Permission.type == 'read'))
print(d)