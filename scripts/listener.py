// SPDX-License-Identifier: BSD-3.0
/*
      Copyright (C) 2020 Yuka Matsuura and Ryuichi Ueda. All right reserved.
*/

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class ListenerNode(Node):  #Nodeクラスの継承
    height = 0
    weight = 0

    def __init__(self):
        super().__init__("Listener")
        self.create_subscription(Float32, "BMI", self.cb, 10)

    def cb(self,msg): #初期化
        if(msg.data <= 2.5): #身長
            #self.get_logger().info("height: %f" % msg.data)
            self.get_logger().info("height: %1.2f" % msg.data)
            self.height = msg.data
        else:                #体重
            self.get_logger().info("weight: %3.2f" % msg.data)
            self.weight = msg.data

        if(self.height != 0 and self.weight != 0):
            self.BMI()

    def BMI(self):
        bmi = self.weight/self.height/self.height
        #BMI = 体重/身長/身長
        self.get_logger().info("BMI : %2.2f" %bmi)
    
rclpy.init()                            
rclpy.spin( ListenerNode() ) #ノードをspinにしかける
