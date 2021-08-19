from behave import *
import os
import requests
import shutil
import utils.ipfs_utils as ipfs_utils

@given('we have IPFS node installed')
def step_impl(context):
    pass

@given('we have TimeRose deployed')
def step_impl(context):
    pass

@when('we add a test file to IPFS')
def step_impl(context):
    target_dir = context.config["TestFileHome"]
    print("target_dir: %s" % target_dir)
    example_file = "example_1.txt"
    ipfs_home = context.config["IpfsHome"]
    indexer_node = context.config["IndexerNode"]
    target_file = target_dir + example_file
    try:
        shutil.copyfile("./resources/test_files/" + example_file, target_file)
    except:
        context.failed = True

    ipfs_bin = ipfs_home + "ipfs"
    console_output = os.popen("%s add --index-node=%s %s" % (ipfs_bin, indexer_node, target_file)).read()
    cids = ipfs_utils.find_cid_from_ipfs_output(console_output, example_file)
    if len(cids) != 1:
        context.failed = True
    context.cid = cids[0]

@then('we can find provider from TimeRose')
def step_impl(context):
    print("CID: %s" % context.cid)
    response = requests.get('http://52.14.211.248:3000/cid/' + context.cid)
    json = response.json()
    print(json)
    cids = json["Cids"]
    assert len(cids) == 1
    cid = cids[0]
    assert cid["Cid"]["/"] == context.cid