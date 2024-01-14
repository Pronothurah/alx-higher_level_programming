#!/usr/bin/python3
'''Creates the State "California" with the City "San Francisco".
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    if len(sys.argv) == 4:
        user = sys.argv[1]
        pword = sys.argv[2]
        db_name = sys.argv[3]

        DATABASE_URL = 'mysql://{}:{}@localhost:3306/{}'.format(
            user, pword, db_name
        )
        engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(engine)

        # Create a session
        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            # Create the State "California" with the City "San Francisco"
            california = State(
                name='California', cities=[City(name='San Francisco')])
            session.add(california)
            session.commit()
            print('State and City added successfully.')
        except Exception as e:
            print(f'Error: {e}')
            session.rollback()
        finally:
            session.close()
    else:
        print('Usage: {} <username> <password> <database_name>'.format(
            sys.argv[0]))
