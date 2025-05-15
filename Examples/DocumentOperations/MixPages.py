# Import modules
import groupdocs_merger_cloud
from Common import Common

# This example demonstrates how to mix specific pages from several source documents
class MixPages:
    @classmethod  
    def Run(cls):
        configuration = Common.GetConfig()
        documentApi = groupdocs_merger_cloud.DocumentApi.from_config(configuration)

        # Prepare file info list
        files = [
            groupdocs_merger_cloud.FileInfo(file_path="WordProcessing/sample-10-pages.docx"),
            groupdocs_merger_cloud.FileInfo(file_path="WordProcessing/four-pages.docx")
        ]

        # Prepare files pages mix items
        files_pages = [
            groupdocs_merger_cloud.MixPagesItem(file_index=0, pages=[1, 2]),
            groupdocs_merger_cloud.MixPagesItem(file_index=1, pages=[1, 2]),
            groupdocs_merger_cloud.MixPagesItem(file_index=0, pages=[3, 4])
        ]

        options = groupdocs_merger_cloud.MixPagesOptions()
        options.files = files
        options.files_pages = files_pages
        options.output_path = "Output/mixed-pages.docx"

        request = groupdocs_merger_cloud.MixRequest(options)
        response = documentApi.mix(request)

        print("Output file path: " + response.path)