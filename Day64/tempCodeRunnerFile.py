
with app.app_context():
    db.session.add(second_movie)
    db.session.commit()