import numpy as np
import tensorflow as tf

N = 7
f = 3
init_v = np.random.randint(0,10,size=(N, f)).astype(np.float32)
C = np.arange(N*N).reshape(N,N).astype(np.float32)
B = tf.ones(shape=(f,1))
ind = tf.constant(np.arange(N).reshape(N,1).astype(np.int32))

queue = tf.FIFOQueue(1000,("int32", "float"))

enq = queue.enqueue_many((ind, C))
i, c = queue.dequeue()

v = tf.Variable(init_v)

c_diag = tf.diag(c)
vt = tf.transpose(v)
v_new = tf.transpose(tf.matmul(tf.matmul(tf.matmul(vt, c_diag),v), B))
update = tf.scatter_update(v, i, v_new)

qr = tf.train.QueueRunner(queue, [enq]*1)

sess = tf.InteractiveSession()
tf.initialize_all_variables().run()
coord = tf.train.Coordinator()

threads = qr.create_threads(sess, coord=coord, start=True)
try:
    for step in range(1000):
        print("step", step)
        if coord.should_stop():
            break
        sess.run(update)
except Exception as e:
    corrd.request_stop(e)

coord.request_stop()
coord.join(threads)
print("success")
quit()
enq.run()


print(queue.size().eval())
print(C)
print(sess.run(v))
sess.run(update)
print(sess.run(v))
sess.run(update)
print(sess.run(v))
