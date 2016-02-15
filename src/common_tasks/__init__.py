# coding: utf-8
import re
import os
from invoke import task, run


@task
def update_requirements(
        path='.',
        pattern=r'^(requirements[^/]*\.in|requirements/.*\.in)$',
        upgrade=True):
    """Compiles requirements.in into requirements.txt using pip-compile
    """
    requirements_files = []

    regex = re.compile(pattern)

    for root, dir, files in os.walk(path):
        for filename in files:
            full_path = os.path.relpath(
                os.path.join(root, filename),
                path)

            if regex.match(full_path) is not None:
                requirements_files.append(full_path)

    for filename in requirements_files:
        command = ['pip-compile']
        if upgrade:
            command.append('--upgrade')
        command.append(filename)
        run(' '.join(command))


def get_current_version():
    """Берет самую последнюю версию из CHANGELOG.md
    Считаем, что она прописана в первой строчке, так:

    ## 0.1.2 (2016-02-13)

    Или без ##.
    """
    with open('CHANGELOG.md') as f:
        first_line = f.readline()
        return first_line.strip('#').split()[0]


def make_dashed_aliases(items):
    """Делает алиасы для invoke тасков, заменяя '_' на '-'.

    Использовать надо так, в конце tasks.py:

    make_dashed_aliases(locals().values())
    """
    for item in items:
        if hasattr(item, 'aliases'):
            item_name = item.__name__
            replaced = item_name.replace('_', '-')
            if replaced != item_name and replaced not in item.aliases:
                item.aliases += (replaced,)
