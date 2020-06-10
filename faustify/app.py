"""
## 使用场景

- Event Processing
- Distributed Joins & Aggregations
- Machine Learning
- Asynchronous Tasks
- Distributed Computing
- Data Denormalization
- Intrusion Detection
- Realtime Web & Web Sockets.
"""
from datetime import datetime
from random import random

import faust

APP_NAME = "faustify"
faustify_app = faust.App(APP_NAME, broker='kafka://localhost', autodiscover=True, origin='faustify.events')


def main():
    faustify_app.main()


if __name__ == '__main__':
    main()
