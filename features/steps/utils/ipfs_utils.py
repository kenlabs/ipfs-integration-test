import re


def find_cid_from_ipfs_output(output, file_name):
    cids = []
    for line in output.split("\n"):
        result = re.search(r"^added ([^\\s]+?) ([^\\s]+?)$", line)
        if result is not None:
            cid = result.group(1)
            file = result.group(2).strip()
            if file_name and file == file_name:
                cids.append(cid)
    return cids