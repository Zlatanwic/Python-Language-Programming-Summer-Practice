from keras.src.utils import *
from keras.src.datasets import mnist # keras集成了mnist数据集
import numpy as np
from keras.src.models import Sequential
from keras.src.layers.core import *
from keras.src.layers.core import dense
from keras.src.layers import Conv2D, MaxPooling2D, Flatten
from keras.src.optimizers import SGD, Adam
#from keras.src.utils import np_utils
from keras.src.utils import *
from tensorflow.python.keras.utils.np_utils import *
#from tensorflow.python.keras.layers.core import dense

import tensorflow
def load_data():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    size = 10000  # 测试集大小
    x_train = x_train[0:size]  # 截取10000个样本
    y_train = y_train[0:size]  # 截取10000个样本
    x_train = x_train.reshape(size, 28 * 28)  # x_train本来是10000x28x28的数组，把它转换成10000x784的二维数组
    x_test = x_test.reshape(x_test.shape[0], 28 * 28)  # 和上面是同一个意思
    x_train = x_train.astype('float32')  # 将它的元素类型转换为float32,之前为uint8
    x_test = x_test.astype('float32')
    # y_train之前可以理解为10000x1的数组，每个单元素数组的值就是样本所表示的数字
    y=tensorflow.python.keras.utils.np_utils
    y_train = tensorflow.python.keras.utils.np_utils(y_train, 10)  # 把它转换成了10000x10的数组
    y_test = tensorflow.python.keras.utils.np_utils.to_categorical(y_test, 10)
    x_train = x_train / 255  # x_train之前的灰度值最大为255，最小为0，这里将它们进行特征归一化，变成了在0到1之间的小数
    x_test = x_test / 255
    return (x_train, y_train), (x_test, y_test)


def run():
    # 加载数据
    (x_train, y_train), (x_test, y_test) = load_data()
    # 定义模型
    model = Sequential()
    # 定义输入层，全连接网络，输入维度是784，有633个神经元，激活函数是Sigmoid
    model.add(dense(input_dim=28 * 28, units=633, activation='sigmoid'))
    # 定义隐藏层
    model.add(dense(units=633, activation='sigmoid'))
    model.add(dense(units=633, activation='sigmoid'))
    # 定义输出层，有10个神经元，也就是10个输出，激活函数是Softmax
    model.add(dense(units=10, activation='softmax'))

    # 损失函数选择均方误差
    model.compile(loss='mse', optimizer=SGD(lr=0.1), metrics=['accuracy'])
    model.fit(x_train, y_train, batch_size=100, epochs=20)

    result = model.evaluate(x_test, y_test)
    print('\nTest Acc:%.2f%%' % (result[1] * 100))


if __name__ == '__main__':
    run()
