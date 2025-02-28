from database.database_alchemy import get_db, engine
from sqlalchemy import Column, String, TIMESTAMP, ForeignKey, Integer, Enum, Boolean
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'

    user_id = Column(String, primary_key=True)
    email = Column(String)
    google_id = Column(String)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    is_admin =  Column(Boolean)

class League(Base):
    __tablename__ = 'League'

    league_id = Column(String(36), primary_key=True)
    name = Column(String(255), nullable=False)
    creator_id = Column(String(36), ForeignKey('User.user_id'), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

class Team(Base):
    __tablename__ = 'Team'

    team_id = Column(String(36), primary_key=True)
    name = Column(String(255), nullable=False, index=True)
    conference = Column(Enum('Eastern', 'Western', name='conference_enum'), nullable=False)
    seed = Column(Integer, nullable=True)
    logo_url = Column(String(255), nullable=True)

class Player(Base):
    __tablename__ = 'Player'

    player_id = Column(String(36), primary_key=True)
    user_id = Column(String(36), ForeignKey('User.user_id'), nullable=False, index=True)
    league_id = Column(String(36), ForeignKey('League.league_id'), nullable=False, index=True)
    name = Column(String(255), nullable=False)
    winning_team_id = Column(String(36), ForeignKey('Team.team_id'), nullable=False, index=True)
    points = Column(Integer, default=0)
    mvp_prediction = Column(String(255), nullable=False)
    joined_at = Column(TIMESTAMP, default=datetime.utcnow)
    is_commissioner = Column(Boolean, nullable=False)

class Matchup(Base):
    __tablename__ = 'Matchup'

    matchup_id = Column(String(36), primary_key=True)
    home_team_id = Column(String(36), ForeignKey('Team.team_id'), nullable=False)
    away_team_id = Column(String(36), ForeignKey('Team.team_id'), nullable=False)
    status = Column(Enum('upcoming', 'in_progress', 'completed', name='status_enum'), 
                   default='upcoming', nullable=False, index=True)
    home_team_score = Column(Integer, default=0)
    away_team_score = Column(Integer, default=0)
    round = Column(Enum('playin_first', 'playin_second', 'first', 'second', 'conference_final', 'final', name='round'), nullable=False)
    conference = Column(Enum('Eastern', 'Western', name='conference_enum'), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)

class Prediction(Base):
    __tablename__ = 'Prediction'

    prediction_id = Column(String(36), primary_key=True)
    player_id = Column(String(36), ForeignKey('Player.player_id'), nullable=False, index=True)
    matchup_id = Column(String(36), ForeignKey('Matchup.matchup_id'), nullable=False, index=True)
    home_team_score = Column(Integer, nullable=False)
    away_team_score = Column(Integer, nullable=False)
    is_correct = Column(Boolean, default=None)
    points_earned = Column(Integer, default=0)
    predicted_at = Column(TIMESTAMP, default=datetime.utcnow)
