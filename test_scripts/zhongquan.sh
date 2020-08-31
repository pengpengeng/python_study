#!/bin/bash
 
for varible1 in {1..100}
do
     echo `netstat -an |grep TIME_WAIT|wc -l`
done
