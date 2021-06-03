# Import modules
import groupdocs_merger_cloud
from Common import Common

# This example demonstrates how to join multiple documents of various formats into one document
class JoinDocumentsCrossFormat:
    @classmethod  
    def Run(cls):
        documentApi = groupdocs_merger_cloud.DocumentApi.from_config(Common.GetConfig())

        item1 = groupdocs_merger_cloud.JoinItem()
        item1.file_info = groupdocs_merger_cloud.FileInfo("Pdf/one-page-password.pdf", None, None, "password")
        item2 = groupdocs_merger_cloud.JoinItem()
        item2.file_info = groupdocs_merger_cloud.FileInfo("WordProcessing/one-page.docx")

        options = groupdocs_merger_cloud.JoinOptions()
        options.join_items = [item1, item2]
        options.output_path = "Output/joined.pdf"

        result = documentApi.join(groupdocs_merger_cloud.JoinRequest(options))        

        print("Output file path = " + result.path)