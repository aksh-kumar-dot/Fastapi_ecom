from fastapi import BackgroundTasks, APIRouter
import time

def write_log(message:str):
    print(f"Background Task:{message}")
    time.sleep(5)
    with open("log.txt",mode="a") as log:
        log.write(f"{message}\n")
    print("BACKGROUND TASK:Completetd writing to log")


router = APIRouter()

@router.post("/send.notifiction/{email}")
def send_notifictions(email:str, background_tasks: BackgroundTasks):
    BackgroundTasks.add_task(write_log,f"sending notifications to{email} with message: it is completed")
    return {"message":"notification will be sent in the background."}
