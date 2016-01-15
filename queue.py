import numpy as np
import tensorflow as tf


queue = tf.FIFOQueue(100, ("int32", "int32"))
tns = tf.constant([[1,2,3],[4,5,6],[7,8,9]])

enq = queue.enqueue_many((tns, tns))

sess = tf.InteractiveSession()

enq.run()
enq.run()
enq.run()
print(queue.size().eval())
deq = queue.dequeue()
x, y = sess.run(deq)
print(x,y)
x, y = sess.run(deq)
print(x,y)
x, y = sess.run(deq)
print(x,y)
x, y = sess.run(deq)
print(x,y)
x, y = sess.run(deq)
print(x,y)
