emails =['ghofraneelkohen@live.fr', 'niwaz@live.fr','ghofghof@gmail.com', 'nawnaw@live.fr']
blacklist =['ghofraneelkohen@live.fr']
for email in emails:
    if email in blacklist:
       print("email {} interdit! envoi impossible.". format(email))
    
    print("email envoyé à", email)

