
from invoke import task
from os.path import exists

@task
def automake(c):
    if not exists('builddir'):
        c.run('CC=clang meson builddir', echo=True, pty=True)

@task(default=True,pre=[automake])
def build(c):
    c.run('ninja -C builddir', echo=True, pty=True)

@task(pre=[automake])
def check(c):
    c.run('ninja -C builddir test', echo=True, pty=True)
