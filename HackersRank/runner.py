import glob, os
import re
import random
import subprocess
import yaml

def get_harness_server_name():
     test_bed = {'name': 'aws-alpha', 'deployment': 'alpha', 'kube_config': '/root/.kube/rnplatform3', 'ssh_user': 'root', 'hosts': [{'name': 'master0', 'host': '10.123.221.190', 'roles': ['master', 'worker']}], 'test_runner': ['test-runner-0', 'test-runner-1', 'opnstk-runner-0', 'opnstk-runner-1'], 'environment': {'cluster_type': 'dev', 'public_fqdn': 'rnplatform3.ciscoiotdev.com', 'public_int_fqdn': 'rnplatform3-int.ciscoiotdev.com', 'csr_hostnames': ['csr0-rnplatform3.ciscoiotdev.com'], 'nlb_int': {'dns_name': 'rnplatform3-udp-nlb-internal.ciscoiotdev.com'}, 's3': {'name': 'rnplatform3-156070148433-dkz5-rainier-bucket', 'arn': 'arn:aws:s3:::rnplatform3-156070148433-dkz5-rainier-bucket'}, 'postgres_service_noistio': 'rnplatform3-rainier-rds.cgxysuh3bvvr.us-west-2.rds.amazonaws.com', 'disable_addons_package': 'True', 'keycloak_login_app_client_secret': 'g8j7^bkd65m-40O?', 'keycloak_infra_client_secret': '2AR6_LM5q7#1c!e4', 'telemetry_client_secret': 'Y1CHi!*63S-7fk04', 'license_client_secret': '23?N.Jm-147Z9KlF', 'pushgateway_url': 'https://pushgateway.rnplatform3.ciscoiotdev.com', 'artifacts': {'keycloak': {'replicas': 2, 'resources': {'limits': {'cpu': '2000m', 'memory': '2Gi', 'ephemeral-storage': '2.5Gi'}, 'requests': {'cpu': '2000m', 'memory': '2Gi', 'ephemeral-storage': '2.5Gi'}}}, 'iam': {'replicas': 2, 'resources': {'limits': {'cpu': '2000m', 'memory': '2Gi', 'ephemeral-storage': '2.5Gi'}, 'requests': {'cpu': '2000m', 'memory': '2Gi', 'ephemeral-storage': '2.5Gi'}}}, 'ui': {'replicas': 2, 'resources': {'limits': {'cpu': '1000m', 'memory': '2Gi', 'ephemeral-storage': '2Gi'}, 'requests': {'cpu': '1000m', 'memory': '2Gi', 'ephemeral-storage': '2Gi'}}}, 'audit': {'replicas': 2, 'resources': {'limits': {'cpu': '2000m', 'memory': '2Gi', 'ephemeral-storage': '2.5Gi'}, 'requests': {'cpu': '2000m', 'memory': '2Gi', 'ephemeral-storage': '2.5Gi'}}}, 'wst': {'replicas': 1, 'resources': {'limits': {'cpu': '2000m', 'memory': '2Gi', 'ephemeral-storage': '2.5Gi'}, 'requests': {'cpu': '2000m', 'memory': '2Gi', 'ephemeral-storage': '2.5Gi'}}}, 'dm': {'replicas': 2, 'resources': {'limits': {'cpu': '3000m', 'memory': '5Gi', 'ephemeral-storage': '25Gi'}, 'requests': {'cpu': '3000m', 'memory': '5Gi', 'ephemeral-storage': '25Gi'}}}, 'jobengmgmt': {'disabled': 'True', 'resources': {'limits': {'cpu': '2000m', 'memory': '2Gi', 'ephemeral-storage': '2.5Gi'}, 'requests': {'cpu': '2000m', 'memory': '2Gi', 'ephemeral-storage': '2.5Gi'}}}, 'csragent': {'resources': {'limits': {'cpu': '1000m', 'memory': '300Mi', 'ephemeral-storage': '300Mi'}, 'requests': {'cpu': '1000m', 'memory': '300Mi', 'ephemeral-storage': '300Mi'}}}, 'qrcode': {'disabled': 'True'}}}, 'repo_version': 'develop'}
     runner_list = test_bed.get('test_runner')
     random.shuffle(runner_list)
     for test_runner_name in runner_list:
        with open("../deployments/"+test_runner_name+".yaml",'r') as file:
         data_loaded = yaml.safe_load(file)
         runner_ip = data_loaded['hosts'][0]['host']
         response = os.system("ping -c 1 " + runner_ip)
         if response == 0:
          container_status = subprocess.Popen("ssh admin@" + runner_ip+ " sudo /usr/local/bin/kubectl get pod -A | grep -i test| grep -i Running | awk '{print $4}' | head -n 1",shell=True, stdout=subprocess.PIPE).stdout
          container_status = container_status.read().decode().strip()
          if container_status == 'Running':
             job_name = subprocess.Popen("ssh admin@" + runner_ip + " sudo /usr/local/bin/kubectl get pod -A | grep -i test | grep -i Running | awk '{print $1}'", shell=True, stdout=subprocess.PIPE).stdout
             job_name = job_name.read().decode().strip()
             print("VM is Reachable but" + job_name + " job is running on the " + runner_ip + " so skipping this VM")
             test_runner_name = get_harness_server_name()
             return test_runner_name
          else:
            print("VM is Reachable and NO test container running on the VM so using " + runner_ip + " for test harness")
            return test_runner_name
         else:
           print(runner_ip + " is not Reachable")
           print("WARNING: please fix the VM")
           test_runner_name = get_harness_server_name()
           return test_runner_name

a = get_harness_server_name()
print(a)