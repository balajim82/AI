from src.database.db import SessionLocal
from src.database.models import InvenotryMgmtOprLog
from datetime import datetime


class InventoryMgmtOprLogRepository:
    def log_action(self, action_name):
        try:
            session = SessionLocal()
            log = InvenotryMgmtOprLog(
                IMOL_ACTION=action_name, IMOL_TIMESTAMP=datetime.now()
            )
            session.add(log)
            session.commit()
            session.close()
        except Exception as e:
            print(
                "In InventoryMgmtOprLogRepository class - log_action Method failed:",
                e,
            )

    def get_all_Log(self):
        try:
            session = SessionLocal()
            data = session.query(InvenotryMgmtOprLog).all()
            session.close()
            return data
        except Exception as e:
            print(
                "In InventoryMgmtOprLogRepository class - get_all_Log Method failed:",
                e,
            )
