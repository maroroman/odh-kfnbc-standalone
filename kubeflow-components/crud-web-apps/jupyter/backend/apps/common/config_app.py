from cmath import log


TESTING_MODE = True

class Logger():

    def info(entry):
        with open("pytest.log", 'w') as log_file:
            log_file.write("[INFO]" + entry)

    def error(entry):
        with open("pytest.log", 'w') as log_file:
            log_file.write("[ERROR]" + entry)

class Mock_API():

    def foo():
        pass