// SPDX-License-Identifier: BSD-3.0
/*
      Copyright (C) 2020 Yuka Matsuura and Ryuichi Ueda. All right reserved.
*/
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

rclpy.init()
node= Node("talker")                               #ノード作成
pub = node.create_publisher(Float32, "BMI", 10)   #パブリッシャ作成

def BMI(): 
    global weight
    global height
    
    msg = Float32()
    msg2 = Float32() 
    
    weight = float(input("How much do yo weight?(Kg)"))
    height = float(input("How tall are you?(m)"))
    
    msg.data = weight
    msg2.data = height

    pub.publish(msg)
    pub.publish(msg2)

node.create_timer(0.5, BMI) #タイマー設定
rclpy.spin(node) #実行
