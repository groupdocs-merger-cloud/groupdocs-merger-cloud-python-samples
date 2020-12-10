# Import modules
import groupdocs_merger_cloud
from Common import Common

# This example demonstrates how to split the document to several one-page documents (by exact page numbers)
class SplitToSinglePages:
    @classmethod  
    def Run(cls):
        documentApi = groupdocs_merger_cloud.DocumentApi.from_config(Common.GetConfig())

        options = groupdocs_merger_cloud.SplitOptions()
        options.file_info = groupdocs_merger_cloud.FileInfo("WordProcessing/sample-10-pages.docx")
        options.output_path = "Output/split-document"
        options.pages = [1, 3]
        options.mode = "Pages"

        result = documentApi.split(groupdocs_merger_cloud.SplitRequest(options))        

        print("Documents count = " + str(len(result.documents)))