#!/usr/bin/python3
'''Lists all City objects from the database.
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    if len(sys.argv) == 4:
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True
        )
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query all City objects with their associated State
        cities = session.query(City).order_by(City.id).all()

        for city in cities:
            print('{}: {} -> {}'.format(city.id, city.name, city.state.name))

        session.close()
