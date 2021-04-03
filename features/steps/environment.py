# pylint: disable=invalid-name
from behave.fixture import use_fixture_by_tag
from dotenv import load_dotenv
from features.steps.setup.setup_platforms import observatory_driver

load_dotenv()

# -- REGISTRY DATA SCHEMA 1: fixture_func
FIXTURE_REGISTRY = {
    "fixture.observatory_driver": observatory_driver
}

def before_tag(context, tag):
    if tag.startswith("fixture."):
        return use_fixture_by_tag(tag, context, FIXTURE_REGISTRY)
    return None
