# Import modules
import groupdocs_merger_cloud
from Common import Common

# This example demonstrates how to remove document password
class RemoveDocumentPassword:
    @classmethod  
    def Run(cls):
        securityApi = groupdocs_merger_cloud.SecurityApi.from_config(Common.GetConfig())

        options = groupdocs_merger_cloud.Options()
        options.file_info = groupdocs_merger_cloud.FileInfo("WordProcessing/password-protected.docx", None, None, "password")
        options.output_path = "Output/remove-password.docx"

        result = securityApi.remove_password(groupdocs_merger_cloud.RemovePasswordRequest(options))

        print("Output file path = " + result.path)