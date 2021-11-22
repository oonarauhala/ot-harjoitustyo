from invoke import task


@task
def start(ctx):
    ctx.run("python3 src/index.py")


@task
def test(ctx):
    ctx.run("poetry shell")
    ctx.run("pytest src")
