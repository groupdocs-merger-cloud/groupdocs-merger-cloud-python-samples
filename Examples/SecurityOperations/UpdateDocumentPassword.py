# Import modules
import groupdocs_merger_cloud
from Common import Common

# This example demonstrates how to update document password
class UpdateDocumentPassword:
    @classmethod  
    def Run(cls):
        securityApi = groupdocs_merger_cloud.SecurityApi.from_keys(Common.app_sid, Common.app_key)

        options = groupdocs_merger_cloud.UpdatePasswordOptions()
        options.file_info = groupdocs_merger_cloud.FileInfo("WordProcessing/password-protected.docx", None, None, "password")
        options.output_path = "Output/update-password.docx"
        options.new_password = "NewPassword"

        result = securityApi.update_password(groupdocs_merger_cloud.UpdatePasswordRequest(options))

        print("Output file path = " + result.path)