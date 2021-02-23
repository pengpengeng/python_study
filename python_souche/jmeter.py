# -*- coding: UTF-8 -*-
import os
import _thread
import time
for i in range(1, 5):
    os.system('sh /Users/zhangpeng/Downloads/apache-jmeter-5.3/bin/jmeter.sh -n -t /Users/zhangpeng/Downloads/易置换_新检测_评估平台存管.jmx -l /Users/zhangpeng/Downloads/666.jtl')
