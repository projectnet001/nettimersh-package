from datetime import datetime
import asyncore
from smtpd import SMTPServer
import threading
import os

class EmlServer(SMTPServer):
    count = 0
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        filename = '%s-%d.eml' % (datetime.now().strftime('%Y%m%d%H%M%S'),
            self.count)
        print(filename)
        f = open(filename, 'wb')
        f.write(data)
        f.close
        print('%s saved.' % filename)
        self.count += 1

def run():
    EmlServer(('localhost', 55678), None)
    print("SMTP server started and running at localhost port 55678")
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass
def exiting():
	while True:
		signal = input("")
		if (signal == "exit"):
			os._exit(1)
if __name__ == '__main__':
    print("When you want to close server just enter exit")
    threadex = threading.Thread(target=exiting)
    threadex.start()
    run()

