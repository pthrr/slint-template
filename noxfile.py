import nox


@nox.session(python=["3.10", "3.11", "3.12"], venv_backend="uv")
def tests(session):
    session.run("uv", "pip", "install", ".", external=True)
    session.run(
        "pytest", "-v", "-s", "--tb=short", "--strict-markers", *session.posargs
    )
