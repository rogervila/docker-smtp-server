import asyncore
import os
from smtpd import DebuggingServer
from sys import stderr


class Server(DebuggingServer):
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        if os.environ.get('SMTP_FAIL') is not None:
            raise Exception('SMTP_FAIL is present. failing...')

        super().process_message(peer, mailfrom, rcpttos, data, **kwargs)
        print(os.linesep, file=stderr)


def main():
    try:
        host = os.environ.get('SMTP_HOST') or '0.0.0.0'
        port = int(os.environ.get('SMTP_PORT') or 25)

        print(
            f'{os.linesep}Running SMTP server on {host}:{str(port)}...{os.linesep}',
            file=stderr
        )

        Server((host, port), None)

        asyncore.loop()
    except KeyboardInterrupt:
        print(
            f'{os.linesep}Keyboard interruption. Stopping...{os.linesep}',
            file=stderr
        )
        pass


if __name__ == '__main__':
    main()
