import glob, os
import re
import random
import subprocess

def get_harness_server_list():
    os.chdir("../deployments")
    runner_list = glob.glob("*runner-[01]*")
    random.shuffle(runner_list)
    return runner_list

def get_harness_server_ip():
  runner_name = get_harness_server_list()[0]
  #print(runner_name)
  runner_name = open(runner_name, 'r').readline().split()[1]
  return runner_name

a = get_harness_server_ip()
print(a)



print("No test container running on the VM so using " + runner_ip + " for test harness")
        print("create automation file")
        filename = "aws-automation.yaml"
        render_vars = {
          "runner_name" : runner_name
         }