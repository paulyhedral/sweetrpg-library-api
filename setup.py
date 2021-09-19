from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="sweetrpg-library-model",
    install_requires=[
        "alembic",
        "Authlib",
        "blinker",
        "dnspython",
        "Flask-Caching",
        "Flask-Cors",
        "Flask-DotEnv",
        "Flask-Inputs",
        "Flask-Migrate",
        "Flask-PyMongo",
        "Flask-REST-JSONAPI",
        "Flask-Script",
        "Flask-Scss",
        "Flask-Session",
        "Flask>=2.0",
        "Jinja2",
        "kanka",
        "PyJWT",
        "pylint",
        "PyMongo[tls]",
        "python-dateutil",
        "python-dotenv",
        "python-editor",
        "PyYAML",
        "redis",
        "requests",
        "sentry-sdk",
        "SQLAlchemy",
        "stripe",
        "sweetrpg-db @ git+https://github.com/sweetrpg/db.git@develop",
        "sweetrpg-library-model @ git+https://github.com/sweetrpg/library-model.git@develop",
        "urllib3",
        "uWSGI",
        "WTForms",
    ],
    extras_require={},
)
