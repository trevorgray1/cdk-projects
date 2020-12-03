import json
import pytest

from aws_cdk import core
from cdk-projects.cdk_projects_stack import CdkProjectsStack


def get_template():
    app = core.App()
    CdkProjectsStack(app, "cdk-projects")
    return json.dumps(app.synth().get_stack("cdk-projects").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
