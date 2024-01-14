#!/usr/bin/python3
'''Changes the name of a State object in the database.
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

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
            # Query the State with id = 2 and update its name
            state_to_update = session.query(State).filter_by(id=2).first()
            if state_to_update:
                state_to_update.name = 'New Mexico'
                session.commit()
                print('State name updated successfully.')
            else:
                print('State with id=2 not found.')
        except Exception as e:
            print(f'Error: {e}')
            session.rollback()
        finally:
            session.close()
    else:
        print('Usage: {} <username> <password> <database_name>'.format(
            sys.argv[0]))
