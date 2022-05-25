import glob, os
import re
import random
import subprocess
import yaml

def get_harness_server_ip():
  runner_list = ['test-runner-0', 'test-runner-1', 'opnstk-runner-0', 'opnstk-runner-1']
  for runner_file in runner_list:
    with open("../deployments/"+runner_file+".yaml",'r') as file:
      data_loaded = yaml.safe_load(file)
      runner_ip = data_loaded['hosts'][0]['host']
  response = os.system("ping -c 1 " + runner_ip)
  if response == 0:
    print("VM is Reachable")
    container_status = subprocess.Popen("ssh admin@" + runner_ip+ " sudo /usr/local/bin/kubectl get pod -A | grep -i test| grep -i Running | awk '{print $4}' | head -n 1",shell=True, stdout=subprocess.PIPE).stdout
    container_status = container_status.read().decode().strip()
    if container_status == 'Running':
        print(container_status)
        job_name = subprocess.Popen("ssh admin@" + runner_ip + " sudo /usr/local/bin/kubectl get pod -A | grep -i test | grep -i Running | awk '{print $1}'", shell=True, stdout=subprocess.PIPE).stdout
        job_name = job_name.read().decode().strip()
        print(job_name + " job is running on the " + runner_ip + " so skipping this VM")
        runner_name = get_harness_server_ip()
        return runner_name
    else:
        #print(container_status)
        print("No test container running on the VM so using " + runner_ip + " for test harness")
        #return runner_name
        print("create automation file")
        filename = job_type + ".yaml"
        render_vars = {
          "runner_name": runner_name
        }
        workdir = os.path.join(os.curdir, "deployments", filename)
        j2_env = Environment(loader=FileSystemLoader(os.curdir), trim_blocks=False)
        #spec = j2_env.get_template('aws-automation.yaml').render(render_vars)
        with open(workdir, 'w') as f:
          f.write(spec)
  else:
      print(runner_ip + " is not Reachable")
      print("WARNING: please fix the VM")
      runner_name = get_harness_server_ip()
      return runner_name


runner_name = get_harness_server_ip()
