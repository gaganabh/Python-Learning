host_name = "new-team-work.example.com"
print("host_name=" + host_name)
splitHostname = host_name.split(".", 1)[0]
print("splitHostname=" + splitHostname)
node_name = splitHostname.split("-", -1)[-1]
print("node_name=" + node_name)
build_name = splitHostname.split("-", -1)[0]
print("build_name=" + build_name)

a = "new-team-work.example.com".rsplit(".", 2)[0].rsplit("-",1)[0]
print(a)