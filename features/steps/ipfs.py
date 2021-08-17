from behave import *
import os
import requests
import shutil

@given('we have IPFS node installed')
def step_impl(context):
    pass

@given('we have TimeRose deployed')
def step_impl(context):
    pass

@when('we add a test file to IPFS')
def step_impl(context):
    target_dir = "/opt/data/"
    example_file = "example_1.txt"
    ipfs_home = "/opt/"
    indexer_node = "http://52.14.211.248:3002"
    target_file = target_dir + example_file
    try:
        shutil.copyfile("./resources/test_files/" + example_file, target_file)
    except:
        context.failed = True

    ipfs_bin = ipfs_home + "ipfs"
    console_output = os.popen("%s add --indexer-node=%s %s" % (ipfs_bin, indexer_node, target_file)).read()

@then('we can find provider from TimeRose')
def step_impl(context):
    response = requests.get('http://52.14.211.248:3000/search/hello.txt')
    print(response.text)
    assert context.failed is False