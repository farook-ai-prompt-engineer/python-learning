class Server:


    def monitor(self):
        print("server monitoring")


class DevOps(Server):


    def deploy(self):
        print("Deploy Application")


engineer = DevOps()

engineer.monitor()
engineer.deploy()
