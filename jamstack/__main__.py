import os
from pathlib import Path

import click
from jamstack.api.file import trycopytree

package_folder = Path(__file__).parent.absolute()
sites_path = os.path.join(package_folder, 'sites')


@click.group(help="<Jamstack cli/>")
def cli():
    pass


@click.command(help="<Empty, plain repo />")
@click.argument('project_name')
@click.option('--existing/--not-existing', default=False)
def plain(project_name, existing):
    path = '.'

    dirs_exist_ok = False
    if existing is True:
        dirs_exist_ok = True
    trycopytree(
        os.path.join(sites_path, 'plain'),
        os.path.join(path, project_name),
        dirs_exist_ok=dirs_exist_ok
    )


@click.command(help="<Repo by templates />")
@click.argument('template')
@click.argument('project_name')
@click.option('--existing/--not-existing', default=False)
def t(template, project_name, existing):
    path = '.'
    templates = {'massively': 'html5up/massively',
                 'phantom': 'html5up/phantom'}

    # namespace = template.split('/')[0]
    # project = template.split('/')[1]

    dirs_exist_ok = False
    if existing is True:
        dirs_exist_ok = True
    trycopytree(
        os.path.join(sites_path, templates[template]),
        os.path.join(path, project_name),
        dirs_exist_ok=dirs_exist_ok
    )


cli.add_command(plain)
cli.add_command(t)


def main():
    cli()


if __name__ == "__main__":
    cli()
