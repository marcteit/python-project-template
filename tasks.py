from invoke import task
import entry_point

@task
def lambda1(ctx):
    entry_point.lambda1()