from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from sqlalchemy import select
from models.models import League

def get_league_by_id(session: Session, league_id: str) -> League:
    try:
        # Fetch the league based on the provided league_id
        league = session.query(League).filter(League.league_id == league_id).one()
        print(f"League Name: {league.name}")
        return league
    except NoResultFound:
        # Handle case where no result is found
        print(f"League with ID {league_id} not found.")
        return None