"""RIOT example application generator module."""

import click

from .common import generate


APPLICATION_PARAMS = {
    "name": {"args": ["Example application name"], "kwargs": {}},
    "brief": {"args": ["Example application brief description"], "kwargs": {}},
    "board": {"args": ["Target board"], "kwargs": {"default": "native"}},
}

APPLICATION_PARAMS_LIST = ["modules", "packages", "features"]

APPLICATION_FILES = ["main.c", "Makefile", "README.md"]


def generate_example(interactive, config, riotbase):
    group = "example"
    params, output_dir = generate(
        group,
        APPLICATION_PARAMS,
        APPLICATION_PARAMS_LIST,
        APPLICATION_FILES,
        interactive,
        config,
        riotbase,
        in_riot_dir="examples",
    )

    click.echo(
        click.style(
            "Example '{name}' generated in {output_dir} with success!".format(
                name=params[group]["name"], output_dir=output_dir
            ),
            bold=True,
        )
    )
