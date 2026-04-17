#!/usr/bin/env python3
"""DB module."""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from user import Base, User


class DB:
    """DB class."""

    def __init__(self) -> None:
        """Initialize a new DB instance."""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object."""
        if self.__session is None:
            db_session = sessionmaker(bind=self._engine)
            self.__session = db_session()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database."""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """Find the first user matching the provided attributes."""
        return self._session.query(User).filter_by(**kwargs).one()

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update a user's attributes."""
        user = self.find_user_by(id=user_id)

        for key, value in kwargs.items():
            if key not in User.__table__.columns:
                raise ValueError
            setattr(user, key, value)

        self._session.commit()
