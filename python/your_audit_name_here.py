"""
This is a template python file for reference use.

DO NOT EDIT THIS FILE.

Copy and rename the copy before modification.

Please include the following template for the top level docstring:

Title:
    - your_audit_name_here
Developed by:
    - Your name yourCec@cisco.com

Description:
    - High Level overview of what the audit does

"""

from datetime import datetime
import time
date_format = "%H:%M:%S.%f"
import ncs

def your_audit_name_here(self, kp, input, name, output):
    """
    This function is used to audit the configurations for an audit action.

    It takes the NSO action params as inputs and returns the updated output object for NSO to use.
    kp = keypath in the NSO application YANG structure (ie the path to your audit)
    input = the input object that includes the data passed into the audit action inside NSO
    name = name of the action. either audit or remediate.
    output = output object that the developer sets and is returned to the user.

    PLEASE ADD A DESCRIPTION OF YOUR CODES LOGIC!

    "Explicit is better than implicit." -- comments are encouraged :)

    """
    if name == "audit":
        start = (datetime.strptime(str(datetime.now().time()), date_format))
        output.start_time = time.strftime("%H:%M:%S")
        with ncs.maapi.single_write_trans("ncsadmin",'python',["ncsadmin"],ip='127.0.0.1', port=ncs.NCS_PORT,path=None, src_ip='127.0.0.1', src_port=0, proto=ncs.PROTO_TCP) as t:
                root = ncs.maagic.get_root(t)
                #
                # Your code goes here
                #
        output.result = "Your results here"
        end = (datetime.strptime(str(datetime.now().time()), date_format))
        output.end_time = time.strftime("%H:%M:%S")
        output.run_time = str(end-start)
    elif name == "remediate":
        self.log.info((uinfo.username))
        start = (datetime.strptime(str(datetime.now().time()), date_format))
        output.start_time = time.strftime("%H:%M:%S")
        with ncs.maapi.single_write_trans("ncsadmin",'python',["ncsadmin"],ip='127.0.0.1', port=ncs.NCS_PORT,path=None, src_ip='127.0.0.1', src_port=0, proto=ncs.PROTO_TCP) as t:
                root = ncs.maagic.get_root(t)
                #
                # Your code goes here
                #
        output.result = "Your results here"
        end = (datetime.strptime(str(datetime.now().time()), date_format))
        output.end_time = time.strftime("%H:%M:%S")
        output.run_time = str(end-start)
    return output
