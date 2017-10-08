from invoke import task
import entry_point
import os

@task
def lambda1(ctx):
    os.environ['a'] = 'b'
    entry_point.lambda1()