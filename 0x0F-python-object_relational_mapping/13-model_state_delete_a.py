#!/usr/bin/python3
'''Deletes State objects with a name containing
the letter 'a' from the database.
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
            # Query and delete State objects with a name containing 'a'
            states_to_delete = session.query(State).filter(
                State.name.like('%a%')).all()
            for state in states_to_delete:
                session.delete(state)

            # Commit the changes
            session.commit()
            print(f'{len(states_to_delete)} State(s) deleted successfully.')
        except Exception as e:
            print(f'Error: {e}')
            session.rollback()
        finally:
            session.close()
    else:
        print('Usage: {} <username> <password> <database_name>'.format(
            sys.argv[0]))
