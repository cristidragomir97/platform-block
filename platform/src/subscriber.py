
import rospy
import threading

class Subscriber(threading.Thread):
    def __init__(self, name, topic, message, callback):
        threading.Thread.__init__(self)
        self.name = name
        self.topic = topic
        self.message = message 
        self.callback = callback

    def run(self):
        rospy.init_node(self.name, anonymous=False, disable_signals=True)
        rospy.Subscriber(self.topic, self.message, self.callback)
        rospy.spin()

        


