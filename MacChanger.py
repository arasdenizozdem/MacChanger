import subprocess
import optparse

parse_obj = optparse.OptionParser()

parse_obj.add_option("-i","--interface",dest="interface",help="interface to change")
parse_obj.add_option("-m","--mac",dest="mac_adress",help="new mac adress")
(user_inputs,arguments) = parse_obj.parse_args()
user_interface= user_inputs.interface
user_mac_adress=user_inputs.mac_adress

subprocess.call(["ifconfig",user_interface,"down"])
subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_adress])
subprocess.call(["ifconfig",user_interface,"up"])