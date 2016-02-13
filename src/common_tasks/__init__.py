__version__ = "0.1.0"

import os
from invoke import task, run


@task
def update_requirements(path='.'):
    """Compiles requirements.in into requirements.txt using pip-compile"""

    for filename in os.listdir(path):
        if filename.endswith('.in'):
            run('pip-compile ' + filename)
