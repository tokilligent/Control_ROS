#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt8
from Tkinter import *

#ROS Code
pub=rospy.Publisher('chatter',UInt8,queue_size=10)
rospy.init_node('talker',anonymous=True)
rate=rospy.Rate(1)
#subscriber msg and commands
def forward(event):
	rospy.loginfo("You're moving FORWARD")
	pub.publish(1)
	rate.sleep()

def forward_left(event):
	rospy.loginfo("You're moving FORWARD_LEFT")
	pub.publish(5)
	rate.sleep()

def forward_right(event):
	rospy.loginfo("You're moving FORWARD_RIGHT")
	pub.publish(6)
	rate.sleep()

def left(event):
	rospy.loginfo("You're moving LEFT")
	pub.publish(2)
	rate.sleep()

def right(event):
	rospy.loginfo("You're moving RIGHT")
	pub.publish(3)
	rate.sleep()

def backward(event):
	rospy.loginfo("You're moving BACK")
	pub.publish(4)
	rate.sleep()

def backward_right(event):
	rospy.loginfo("You're moving BACKWARD_RIGHT")
	pub.publish(7)
	rate.sleep()

def backward_left(event):
	rospy.loginfo("You're moving BACKWARD_LEFT")
	pub.publish(8)
	rate.sleep()

def stop(event):
	rospy.loginfo("You're Stopped")
	pub.publish(0)
	rate.sleep()

#ROS code's main body
if __name__=='__main__':
	
	try:
        #GUI CODE
		root=Tk()
		root.title("MongolTori")
		root.geometry("600x200")
		root.configure(background="white")
		#key for moving
		root.bind("w", forward)
		root.bind("q", forward_left)
		root.bind("e", forward_right)
		root.bind("s", backward)
		root.bind("z", backward_left)
		root.bind("c", backward_right)
		root.bind("a", left)
		root.bind("d", right)
		root.bind("f", stop)
		
		w = Button(root, text="Forward",bg="black",fg="white",command=forward)
		w.grid(row=0, column=4)

		q = Button(root, text="Forward Left",bg="black",fg="white",command=forward_left)
		q.grid(row=0, column=3)

		e = Button(root, text="Forward Right",bg="black",fg="white",command=forward_right)
		e.grid(row=0, column=5)

		s = Button(root, text="Backward",bg="black",fg="white",command=backward)
		s.grid(row=2, column=4)

		z = Button(root, text="Backward Left",bg="black",fg="white",command=backward_left)
		z.grid(row=2, column=3)

		c = Button(root, text="Backward Right",bg="black",fg="white",command=backward_right)
		c.grid(row=2, column=5)

		a = Button(root, text="Left",bg="black",fg="white",command=left)
		a.grid(row=1, column=3)

		d = Button(root, text="Right",bg="black",fg="white",command=right)
		d.grid(row=1, column=5)

		stop = Button(root, text="Stop",bg="black",fg="white",command=stop)
		stop.grid(row=1, column=4)

		slider = Scale(root, from_=0, to=200, orient=HORIZONTAL)
		slider.grid(row=1, column=0)


		speed = Label(root,text="Speed",bg="white")
		speed.grid(row=2,column=0)

		root.mainloop()
	
	except rospy.ROSInterruptException:
		pass