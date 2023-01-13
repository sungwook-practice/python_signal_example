import threading
import signal
import time

def signal_handler(signum, frame):
    print("Signal received.")

def child_thread():
    print("Child thread started")
    while True:
        time.sleep(1)
        print("Child thread is running.")

# # register the signal handler
# signal.signal(signal.SIGINT, signal_handler)

# start the child thread
child_thread = threading.Thread(target=child_thread)
child_thread.start()

# wait for the child thread to finish
child_thread.join()
