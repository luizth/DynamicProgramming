import time


class ConsoleStyle:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def show_break_line():
        print()

    @staticmethod
    def delay():
        time.sleep(3)

    @staticmethod
    def show_message_default(msg, br: bool = True):
        ConsoleStyle.__show_message(msg, br, ConsoleStyle.ENDC)

    @staticmethod
    def show_message_fail(msg, br: bool = True):
        ConsoleStyle.__show_message(msg, br, ConsoleStyle.FAIL + ConsoleStyle.BOLD)

    @staticmethod
    def show_message_success(msg, br: bool = True):
        ConsoleStyle.__show_message(msg, br, ConsoleStyle.OKGREEN)

    @staticmethod
    def __show_message(msg: str, br: bool, style: str):
        print(f'{style}{msg}{ConsoleStyle.ENDC}', end=('\n' if br else ''))
