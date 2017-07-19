"""
This is a template python file for reference use.

DO NOT EDIT THIS FILE.

Copy and rename the copy before modification.

Please include the following template for the top level docstring:

Title:
    - your_module_name_here

Developed by:
    - Your name yourCec@cisco.com

Description:
    - High Level overview of what the audit does

"""

import ncs
from .abs_audit import AbsAudit

class YourModuleNameHere(AbsAudit):

    def __init__(self):
        self.group = "IPv6"

    def audit(self, devices, output):
        pass # YOUR AUDIT CODE HERE!

    def remediate(self, devices, output):
        pass # YOUR REMDIATE CODE HERE!