# import numpy as np
# from matplotlib import pyplot as plt


# x = np.arange(100)/100
# delta = np.random.uniform(-0.05, 0.05, size=(100,))
# y = 0.4 * x + 0.7 + delta

# w = np.random.random()
# b = np.random.random()

# y_pred = b + w*x

# def plot_reg(x, y, y_pred):
#     plt.scatter(x, y, color = "m",marker = "o", s = 30)
#     plt.plot(x, y_pred, color = "g")
#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.pause(0.1)
    
# plot_reg (x, y, y_pred)


# def training(x, y, w, b, lr, nb_epochs):
#     all_loss = []
#     for i in range(nb_epochs):
#         print('epoch: ', i)
#         prediction = x*w + b
#         loss = np.mean((y - prediction)**2)
#         all_loss.append(loss)
#         #loss = np.sum((y - prediction)**2)/len(x)
#         print('loss: ', loss)
        
#         grad_w = -(2/len(x))*np.sum(x*(y - prediction))
#         grad_b = -(2/len(x))*np.sum(y - prediction)
        
#         w = w - lr*grad_w
#         b = b - lr*grad_b
        
#         print('w: ', w)
#         print('b: ', b)
        
#         if i%10 == 0:
#             y_pred = b + w*x
#             plot_reg(x, y, y_pred)
        
#     return w, b, all_loss
        
# w, b, all_loss = training(x, y, w, b, 0.05, 500)     

# y_pred = b + w*x

# plt.figure()
# plot_reg(x, y, y_pred)
        
# plt.figure()
# plt.plot(np.arange(500), all_loss)

























import numpy as np
from matplotlib import pyplot as plt
import tensorflow as tf


x = np.arange(100)/100
delta = np.random.uniform(-0.05, 0.05, size=(100,))
y = 0.4 * x + 0.7 + delta




my_model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(1,)),
    tf.keras.layers.Dense(units=1, activation='linear')
])

my_model.summary()


pred = my_model.predict(x)
plt.figure()
plt.scatter(x, y, color = "m",marker = "o", s = 30)
plt.plot(x, pred, color = "g")


my_model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.1),
    loss='mean_squared_error')



history = my_model.fit(
    x,
    y,
    100,
    epochs=100,
    verbose=1,
    validation_split = 0.2)


pred = my_model.predict(x)
plt.figure()
plt.scatter(x, y, color = "m",marker = "o", s = 30)
plt.plot(x, pred, color = "g")