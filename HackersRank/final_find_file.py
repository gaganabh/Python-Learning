import glob, os
import re
import random
import subprocess
#from jinja2 import Environment, FileSystemLoader

def get_harness_server_list():
    os.chdir("../deployments")
    runner_list = glob.glob("*runner-[01]*")
    random.shuffle(runner_list)
    return runner_list

def get_harness_server_ip():
  runner_file = get_harness_server_list()[0]
  runner_name = open(runner_file, 'r').readline().split()[1]
  runner_file = open(runner_file, 'r')
  for runner_host in runner_file.readlines():
    if re.search('host:', runner_host):
       runner_ip = (runner_host).split(":",1)[1]
       runner_ip = runner_ip.strip()
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






