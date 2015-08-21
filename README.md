Fabric
=========

Configure fabric on Centos.

Role Variables
--------------

Here is the list of all variables and their default values:

If you want to install minimum set of fablic, change the fabric_install_options to False.

    fabric_install_options: True

The following settings decided who executes fabric commands.

    fabric_user: vagrant
    fabric_group: vagrant
    fabric_home: /home/vagrant

The environment configurations control Fabric's behavior.

    fabric_warn_only: True

Dependencies
------------

- bobbyrenwick.pip

Example Playbook
----------------

    - hosts: test
      sudo: yes
      remote_user: vagrant
      roles:
              - { role: ynaka81.fabric }

License
-------

BSD
