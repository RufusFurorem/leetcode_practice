class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.msg_queue = []
        self.msg_time  = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.msg_time:
            self.msg_time[message] = timestamp

        if timestamp - self.msg_time[message] >= 10:
            self.msg_queue.remove(message)
        
        if message in self.msg_queue:
            return False
        else:
            self.msg_queue.append(message)
            self.msg_time[message] = timestamp
                 
        return True