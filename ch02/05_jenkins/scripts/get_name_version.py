#!/usr/bin/env python

import jenkins

server = jenkins.Jenkins('https://ci.jenkins.net', username='mine', password='dee3f1161b76f1e796f517e0c902bd5c8b')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' %(user['fullName'], version))
