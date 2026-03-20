from src.database.db import SessionLocal
from src.database.models import InvenotryMgmtOprLog
from datetime import datetime


class InventoryMgmtOprLogRepository:
    def log_action(self, action_name):
        session = SessionLocal()
        log = InvenotryMgmtOprLog(
            IMOL_ACTION=action_name, IMOL_TIMESTAMP=datetime.now()
        )
        session.add(log)
        session.commit()
        session.close()

    def get_all_Log(self):
        session = SessionLocal()
        data = session.query(InvenotryMgmtOprLog).all()
        session.close()
        return data
