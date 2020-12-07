import uiautomator2
import unittest
import subprocess
import time
import re

def run_shell_command(cmd):
    return subprocess.run(cmd, shell=True, check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

class uiauto():
    def __init__(self,ip):
        self.ip = ip
        self.device = uiautomator2.connect(ip)

    def click_by_text(self, text, contains=False, timeout=2):
        if contains:
            return self.device(textcontains=text).click_exists(timeout)
        return self.device(text=text).click_exists(timeout)

    def click_by_resourceId(self, resourceId, timeout):
        return self.device(resourceId=resourceId).click_exists(timeout)

    def click_by_resourceId(self, resourceId, timeout):
        return self.device(resourceId=resourceId).click_exists(timeout)

    def click_by_resourceId(self, resourceId, timeout):
        return self.device(resourceId=resourceId).click_exists(timeout)

    def click_by_resourceId(self, resourceId, timeout):
        return self.device(resourceId=resourceId).click_exists(timeout)