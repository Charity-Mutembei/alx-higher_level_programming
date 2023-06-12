a = {'id': 89, 'friends': [{'id': 82, 'name': "Bob"}, {'id': 83, 'name': "Amy"}]}
print(a.get('friends')[-1].get("name"))