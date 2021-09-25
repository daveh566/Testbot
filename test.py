users = await client.get_participants(chat)
print(users[0].first_name)

for user in users:
    if user.username is not None:
        print(user.username)
