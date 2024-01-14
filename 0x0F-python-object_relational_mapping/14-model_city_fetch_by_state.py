#!/usr/bin/python3
'''Prints all City objects from the database.
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    if len(sys.argv) == 4:
        user = sys.argv[1]
        pword = sys.argv[2]
        db_name = sys.argv[3]

        DATABASE_URL = f"mysql://{user}:{pword}@localhost:3306/{db_name}"
        engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(engine)

        # Create a session
        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            # Query all City objects and print the results
            cities = session.query(City).order_by(City.id).all()
            for city in cities:
                print('{}: ({}) {}'.format(
                    city.state.name, city.id, city.name))
        except Exception as e:
            print(f'Error: {e}')
        finally:
            session.close()
    else:
        print('Usage: {} <username> <password> <database_name>'.format(
            sys.argv[0]))
