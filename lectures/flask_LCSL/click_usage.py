import click


@click.command('hello')
def hello():
    val = click.prompt('say hello', type=str, default="hello")
    print(val)


@click.command('boom')
def boom():
    if click.confirm('do you wanna boom your database?'):
        click.echo('Whell done! Your database just gone!')


@click.command()
@click.confirmation_option(prompt='Drop prod db')
def dropdb():
    click.echo('Fine! Now you can seek for a new job in construction area :)')


if __name__ == '__main__':
    boom()
