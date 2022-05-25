import os
import glob
import subprocess
import random


runner_filenames = []
os.chdir("../deployments")
runner_filenames = glob.glob("*-runner-*")

def get_harness_server_state():
  os.chdir("../deployments")
  runner_filenames = glob.glob("*-runner-*")
  random.shuffle(runner_filenames)
  return runner_filenames[0]

  response = os.system("ping -c 1 " + hostname)  # ping check
  if response == 0:
    print("VM is Reachable")
    container_status = subprocess.Popen("ssh admin@" + first + " sudo /usr/local/bin/kubectl get pod -A | grep -i test| grep -i Running | awk '{print $4}' | head -n 1", shell=True, stdout=subprocess.PIPE).stdout
    container_status = container_status.read().decode()
    print(container_status)
    if container_status != 'Running' :
      print("No test container running on the VM so using "+hostname+ " for test harness")
      return hostname
    else:
      job_name = subprocess.Popen(
        "ssh admin@" + first + " sudo /usr/local/bin/kubectl get pod -A | grep -i test | grep -i Running | awk '{print $1}'",
        shell=True, stdout=subprocess.PIPE).stdout
      job_name = job_name.read().decode()
      print(job_name + " is running on the " + hostname)

  else:
    print(hostname + " is not Reachable")
    print("WARNING: please fix the VM")



  ip_file.write(lines)
  ip_file.write(first)
  ip_file.close()

check_harness_vm_state()