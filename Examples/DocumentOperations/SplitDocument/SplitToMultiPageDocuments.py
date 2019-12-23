# Import modules
import groupdocs_merger_cloud
from Common import Common

# This example demonstrates how to split the document to several multi-page documents by specified page ranges
class SplitToMultiPageDocuments:
    @classmethod  
    def Run(cls):
        documentApi = groupdocs_merger_cloud.DocumentApi.from_keys(Common.app_sid, Common.app_key)

        options = groupdocs_merger_cloud.SplitOptions()
        options.file_info = groupdocs_merger_cloud.FileInfo("WordProcessing/sample-10-pages.docx")
        options.output_path = "Output/split-to-multipage-document"
        options.pages = [2, 4]
        options.mode = "Intervals"

        result = documentApi.split(groupdocs_merger_cloud.SplitRequest(options))        

        print("Documents count = " + str(len(result.documents)))