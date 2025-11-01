import logging
from main import log_event

def test_success_written_to_file():
    logger = logging.getLogger("log_event")
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler("login_system.log")
    logger.addHandler(file_handler)
    log_event("Diana", "success")
    file_handler.close()

    with open("login_system.log", "r") as f:
        text = f.read()
    assert "Login event - Username: Diana, Status: success" in text

def test_expired_written_to_file():
    logger = logging.getLogger("log_event")
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler("login_system.log")
    logger.addHandler(file_handler)
    log_event("User1", "expired")
    file_handler.close()

    with open("login_system.log", "r") as f:
        text = f.read()
    assert "Login event - Username: User1, Status: expired" in text

def test_failed_written_to_file():
    logger = logging.getLogger("log_event")
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler("login_system.log")
    logger.addHandler(file_handler)
    log_event("User2", "failed")
    file_handler.close()

    with open("login_system.log", "r") as f:
        text = f.read()
    assert "Login event - Username: User2, Status: failed" in text