# ros2_BMI
kadai2

## ROS2でBMIの計算を行う

- BMI=体重/身長/身長


## 使用した環境
- Raspberry Pi 4 ModelB
- ROS2 : foxy
- OS : Ubuntu20.04
- 言語 : python3.8

## ROS2のインストールについて
https://github.com/ryuichiueda/ros2_setup_scripts

## プログラムの実行方法

スクリプトの置き場は　~/ros2_ws/src/mypkg/mypkg

```
$ git clone https://github.com/Chanman3/ros2_BMI.git
$ chmod +x talker.py
$ chmod +x listener.py
$ cd ~/ros2_ws
$ sudo rosdep install -i --from-path src --rosdistro foxy -y
$ colcon build
$ . install/setup.bash
```


## 動画説明

１. 端末を2つ立ち上げ，　ros2_ws　に移動する．

- 端末1　
```
$ ros2 run mypkg talker
```

- 端末2
```
$ ros2 run mypkg listener
```

２．端末1側で，身長と体重についてそれぞれ単位に沿って入力しEnterを押す．

- 端末1(入力例)
```
How much do yo weight?(Kg)46
How tall are you?(m)1.5
```

３．端末2側で、入力した身長と体重、計算されたBMI値が表示される．

-端末2(出力例)　
```
[INFO] [1610101500.790445324] [Listener]: weight: 46.00
[INFO] [1610101500.793357840] [Listener]: height: 1.50
[INFO] [1610101500.795387733] [Listener]: BMI : 20.44
```



## デモ動画

https://youtu.be/l-sZJ4__t_E
