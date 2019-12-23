# Import modules
import groupdocs_merger_cloud
from Common import Common

# This example demonstrates how to check document password
class CheckDocumentPasswordProtection:
    @classmethod  
    def Run(cls):
        securityApi = groupdocs_merger_cloud.SecurityApi.from_keys(Common.app_sid, Common.app_key)

        result = securityApi.check_password(groupdocs_merger_cloud.CheckPasswordRequest("WordProcessing/password-protected.docx"))

        print("Check password = " + str(result.is_password_set))