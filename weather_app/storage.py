from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class SearchHistory(Base):
    __tablename__ = "weather_history"

    id = Column(Integer, primary_key=True)
    city = Column(String)
    temperature = Column(Float)
    condition = Column(String)
    searched_at = Column(DateTime, default=datetime.now)

    def __str__(self):
        return f"{self.city} ({self.created_at.strftime('%H:%M')})"


class DatabaseManager:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)

        Base.metadata.create_all(self.engine)

        self.Session = sessionmaker(bind=self.engine)

    def save_report(self, report):
        session = self.Session()
        history_item = SearchHistory(
            city=report.city, temperature=report.temperature, condition=report.condition
        )

        session.add(history_item)
        session.commit()
        session.close()
        print("Saved to ur DataBase!")

        def get_history(self):
            session = self.Session()
            result = (
                session.query(SearchHistory)
                .order_by(SearchHistory.created_at.desc())
                .limit(5)
                .all()
            )
