# Import modules
import groupdocs_merger_cloud
from Common import Common

# This example demonstrates how to get document info
class GetInfo:
    @classmethod  
    def Run(cls):
        infoApi = groupdocs_merger_cloud.InfoApi.from_keys(Common.app_sid, Common.app_key)
        fileInfo = groupdocs_merger_cloud.FileInfo("WordProcessing/password-protected.docx", None, None, "password")
        result = infoApi.get_info(groupdocs_merger_cloud.GetInfoRequest(fileInfo))        
        print("Page count = " + str(len(result.pages)))