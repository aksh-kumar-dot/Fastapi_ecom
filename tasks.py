<<<<<<< HEAD
import time
from sqlalchemy.orm import session
from worker import celery_app
from core.db import get_session
from model.models import Order
from sqlalchemy import create_engine
from core.config import settings
from sqlmodel import select


engine=create_engine(settings.DATABASE_SYNC_URL,echo=True)

STAGES=["Packing","Shipping","Delivered"]

def get_sync_session():
    with session(engine) as session:
        yield session

@celery_app.task
def process_order(order_id:int):
    session=next(get_sync_session())

    try:
        order=session.exec(select(Order).where(Order_id==order_id)).first()
        if not order:
            return {"eerror":"order not found"}
        
        for stage in STAGES:
            time.sleep(10)
            order.status=stage
            session.add(order)
            session.commit()
            session.refresh(order)

        return {"order_id":order_id,"final_status":order.status}
    finally:
        session.close()
=======
import time
from sqlalchemy.orm import session
from worker import celery_app
from core.db import get_session
from model.models import Order
from sqlalchemy import create_engine
from core.config import settings
from sqlmodel import select


engine=create_engine(settings.DATABASE_SYNC_URL,echo=True)

STAGES=["Packing","Shipping","Delivered"]

def get_sync_session():
    with session(engine) as session:
        yield session

@celery_app.task
def process_order(order_id:int):
    session=next(get_sync_session())

    try:
        order=session.exec(select(Order).where(Order_id==order_id)).first()
        if not order:
            return {"eerror":"order not found"}
        
        for stage in STAGES:
            time.sleep(10)
            order.status=stage
            session.add(order)
            session.commit()
            session.refresh(order)

        return {"order_id":order_id,"final_status":order.status}
    finally:
        session.close()
>>>>>>> dev-docker-swarm
