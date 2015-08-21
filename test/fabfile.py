import yaml
from fabric.api import task, run, env, execute

## Set deploy target environment
# @param target target enironment
def setTarget(target):
    # set deploy target from target.yml
    targets = yaml.load(file("target.yml"))
    env.hosts = targets[target]["hosts"]
    env.user = targets[target]["user"]
    env.password = targets[target]["password"]

## hello fabric main logic
def sayHelloFabric():
    run("echo Hello Fabric at `hostname`!")

## test intarface for fabric command line tool
# @param target target environment
@task
def helloFabric(target):
    setTarget(target)
    execute(sayHelloFabric)
