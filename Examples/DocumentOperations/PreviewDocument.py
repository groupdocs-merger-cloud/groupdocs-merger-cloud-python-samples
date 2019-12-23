# Import modules
import groupdocs_merger_cloud
from Common import Common

# This example demonstrates how to generate document pages preview
class PreviewDocument:
    @classmethod  
    def Run(cls):
        documentApi = groupdocs_merger_cloud.DocumentApi.from_keys(Common.app_sid, Common.app_key)

        options = groupdocs_merger_cloud.PreviewOptions()
        options.file_info = groupdocs_merger_cloud.FileInfo("WordProcessing/four-pages.docx")
        options.output_path = "Output/preview-page"
        options.pages = [1, 3]
        options.format = "Png"

        result = documentApi.preview(groupdocs_merger_cloud.PreviewRequest(options))        

        print("Documents count = " + str(len(result.documents)))