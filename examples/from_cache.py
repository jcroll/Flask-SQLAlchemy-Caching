from flask_sqlalchemy import get_debug_queries
from flask_sqlalchemy_caching import FromCache

from _base import app, cache, Country

with app.app_context():
    q = Country.query.order_by(Country.id.asc())
    caching_q = q.options(FromCache(cache))

    country = caching_q.first()
    assert 'Brazil' == country.name
    # assert 'Germany' == countries[1].name
    print('{} queries executed.'.format(len(get_debug_queries())))
