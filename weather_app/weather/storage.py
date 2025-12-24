from database import SessionLocal  # Import the connection tool
from weather.models import SearchHistory  # Import the table definition


class WeatherStorage:
    def save_report(self, report):
        # 1. Get a fresh worker
        session = SessionLocal()

        try:
            history_item = SearchHistory(
                city=report.city,
                temperature=report.temperature,
                condition=report.condition,
            )
            session.add(history_item)
            session.commit()
            print("✅ Weather saved!")
        except Exception as e:
            print(f"Error saving: {e}")
            session.rollback()
        finally:
            session.close()

    def get_history(self):
        session = SessionLocal()
        try:
            # We query the model we imported
            results = (
                session.query(SearchHistory)
                .order_by(SearchHistory.searched_at.desc())
                .limit(5)
                .all()
            )
            return results
        finally:
            session.close()
