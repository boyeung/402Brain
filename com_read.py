#coding=utf-8

import serial
import time
import struct
ser = serial.Serial('COM2', 115200) #设置串口参数

ser.write("\x01\x00\x00\x01\x00\x00\x00\x00") #通过串口给信号发生器发送命令

time.sleep(1) #休眠0.1秒，等待信号发生器对上述命令的应答,可以删除此语句

#通过串口读取信号发生器的数据，例如循环读取50个字节
data = ser.read(3508) #每次读取一个字节的数据
# char,=struct.unpack("b", data) #将接收的字节流转化为Python能使用的数值，该函数返回的是一个tuple."b"表示signed char，转换之后编程python中的integer
# print char,

