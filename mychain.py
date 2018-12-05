import signal
from app import user_interface
from app import app_controller


def signal_handler(_signal, frame):
    app_controller.finish_app()


# todo PEER의 IP를 등록함
ip_list = ["70.12.113.119", "70.12.113.222"]
app_controller.start_app(ip_list, isPrivate=True)

# 앱 종료를 위한 시그널 생성 (ctrl+c)
signal.signal(signal.SIGINT, signal_handler)

# 메뉴 호출
user_interface.main_menu()
