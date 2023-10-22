def insert_data():
    #------------------------
    user1 = User(name='Rodion', username='IamRodion')
    user2 = User(name='Carlos', username='CarSa123')
    user3 = User(name='Aura', username='AuraSenpaii')

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)

    db.session.commit()
    #------------------------
    item1 = Item(name='Helmet')
    item2 = Item(name='Armour')
    item3 = Item(name='Gloves')
    item4 = Item(name='Boots')

    db.session.add(item1)
    db.session.add(item2)
    db.session.add(item3)
    db.session.add(item4)

    db.session.commit()
    #------------------------
    trade1 = Trade(user_id=user1.id, item_id=item2.id, price=15.5)
    trade2 = Trade(user_id=user2.id, item_id=item3.id, price=25)
    trade3 = Trade(user_id=user1.id, item_id=item3.id, price=115)
    trade4 = Trade(user_id=user3.id, item_id=item1.id, price=5.2)
    trade5 = Trade(user_id=user3.id, item_id=item2.id, price=7.3)
    trade6 = Trade(user_id=user2.id, item_id=item4.id, price=200)

    db.session.add(trade1)
    db.session.add(trade2)
    db.session.add(trade3)
    db.session.add(trade4)
    db.session.add(trade5)
    db.session.add(trade6)

    db.session.commit()