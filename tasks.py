from invoke import task
from invoke import run
import entry_point
import os
import zipfile

@task
def lambda1(ctx):
    os.environ['a'] = 'b'
    entry_point.lambda1()

@task
def build(ctx):
    run('pip install -r requirements.txt -t .', hide=True)
    build_file = zipfile.ZipFile('build.zip', 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk('.'):
        if root.find('.git') == -1:
            for file in files:
                build_file.write(os.path.join(root, file))
    build_file.close()