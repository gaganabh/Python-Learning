import glob, os
import re
import random
import subprocess

runner_filename = []

def get_harness_server_state():
    os.chdir("../deployments")
    runner_filename = glob.glob("*runner-[01]*")
    random.shuffle(runner_filename)
    print(runner_filename)
    return runner_filename[0]


runner_filename = get_harness_server_state()
runner_filename = open(runner_filename, 'r')
for line in runner_filename.readlines():
    if re.search('host:', line, re.M):
        ip = (line).split(':', 1)[1]
        ip = ip.strip()
        print(ip)


response = os.system("ping -c 1 " + ip)

if response == 0:
  print("VM is Reachable")
  container_status = subprocess.Popen(
    "ssh admin@" + ip+ " sudo /usr/local/bin/kubectl get pod -A | grep -i test| grep -i Running | awk '{print $4}' | head -n 1",
    shell=True, stdout=subprocess.PIPE).stdout
  container_status = container_status.read().decode().strip()
  if container_status == 'Running':
    print(container_status)
    job_name = subprocess.Popen("ssh admin@" + ip + " sudo /usr/local/bin/kubectl get pod -A | grep -i test | grep -i Running | awk '{print $1}'", shell=True, stdout=subprocess.PIPE).stdout
    job_name = job_name.read().decode().strip()
    print(job_name + " job is running on the " + ip)

  else:
    print(container_status)
    print("No test container running on the VM so using " + ip + " for test harness")
else:
  print(ip + " is not Reachable")
  print("WARNING: please fix the VM")
