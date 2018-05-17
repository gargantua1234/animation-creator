import uuid


def gerate_name(file_name):
  return "{}/{}/{}".format("upload", uuid.uuid4(),  file_name)
