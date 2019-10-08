girder.nginx
============
[![Apache 2.0](https://img.shields.io/badge/license-Apache%202-blue.svg)](https://raw.githubusercontent.com/girder/ansible-role-girder-nginx/master/LICENSE)
[![Tests](https://circleci.com/gh/girder/ansible-role-girder-nginx.svg?style=svg)](https://circleci.com/gh/girder/ansible-role-girder-nginx)

An Ansible role to install Nginx, with HTTPS support, and configure it
for use with Girder.

Requirements
------------

Ubuntu 18.04+.

The target must be reachable from the internet via the domain name
`nginx_hostname`.

The target machine should also be able to initiate outgoing UDP
connections  from port 53 to the internet, for DNS resolution and OCSP
stapling. Many firewalls (e.g. the
[AWS EC2 default security group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html#default-security-group))
do not allow this by default.

Role Variables
--------------

| parameter                   | required | default              | comments                                                                |
| --------------------------- | -------- | -------------------- | ----------------------------------------------------------------------- |
| `nginx_hostname`            | yes      |                      | The hostname of the site. `{{ inventory_hostname }}` may provide this.  |
| `nginx_registration_email`  | no       | `girder@kitware.com` | The email address to register with Let's Encrypt for expiration alerts. |
| `nginx_extra_server_config` | no       |                      | Any extra Nginx configuration to add to the `server` block for Girder.  |

Dependencies
------------

This role does not have any formal dependencies, but is intended to be
used in conjunction with the
[`girder.girder` role](https://galaxy.ansible.com/girder/girder).


Example Playbook
----------------

A typical playbook using this role may look like:

```yaml
- name: Deploy public-facing Girder
  hosts: all
  vars:
    ansible_python_interpreter: auto
  roles:
    - role: girder.mongodb
    - role: girder.girder
    - role: girder.nginx
      vars:
        nginx_hostname: data.girder.org
```

License
-------

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0.html)
