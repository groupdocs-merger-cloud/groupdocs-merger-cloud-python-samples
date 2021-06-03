# Import modules
import groupdocs_merger_cloud
from Common import Common

# This example demonstrates how to import attachment into pdf document
class ImportAttachment:
    @classmethod  
    def Run(cls):
        documentApi = groupdocs_merger_cloud.DocumentApi.from_config(Common.GetConfig())

        options = groupdocs_merger_cloud.ImportOptions()
        options.file_info = groupdocs_merger_cloud.FileInfo("Pdf/one-page-password.pdf", None, None, "password")
        options.attachments = ["Txt/document.txt"]
        options.output_path = "Output/with-attachment.pdf"

        result = documentApi.call_import(groupdocs_merger_cloud.CallImportRequest(options))

        print("Output file path = " + result.path)
