# Import modules
import groupdocs_merger_cloud
from Common import Common

# This example demonstrates how to add password to document
class AddDocumentPassword:
    @classmethod  
    def Run(cls):
        securityApi = groupdocs_merger_cloud.SecurityApi.from_keys(Common.app_sid, Common.app_key)

        options = groupdocs_merger_cloud.Options()
        options.file_info = groupdocs_merger_cloud.FileInfo("WordProcessing/one-page.docx", None, None, "password")
        options.output_path = "Output/add-password.docx"

        result = securityApi.add_password(groupdocs_merger_cloud.AddPasswordRequest(options))

        print("Output file path = " + result.path)