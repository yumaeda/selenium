# -*- coding: utf-8 -*-
"""Pythonのタスクランナー"""

from invoke import task

@task
def clean(c, bytecode=False, extra=''):
    """クリーンアップ処理"""
    patterns = ['build']
    if bytecode:
        patterns.append('**/*.pyc')
    if extra:
        patterns.append(extra)
    for pattern in patterns:
        c.run("rm -rf {}".format(pattern))

@task
def build(c):
    """ビルド＆Linting処理"""
    c.run('pylint src/*.py')
    c.run('python -m compileall src/*.py')
    c.run('mkdir build')
    c.run('mv src/*.pyc build')
