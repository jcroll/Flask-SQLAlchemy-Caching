from flask_sqlalchemy import get_debug_queries
from flask_sqlalchemy_caching import RelationshipCache

from _base import app, cache, db, State, City

with app.app_context():
    rc = RelationshipCache(State.country, cache)
    q = City.query.options(db.joinedload(City.state), rc)
    for item in q:
        assert "Brazil" == item.state.country.name
    print('{} queries executed.'.format(len(get_debug_queries())))
