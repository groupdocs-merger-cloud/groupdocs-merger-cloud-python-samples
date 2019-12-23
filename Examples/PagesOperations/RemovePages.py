# Import modules
import groupdocs_merger_cloud
from Common import Common

# This example demonstrates how to remove document pages
class RemovePages:
    @classmethod  
    def Run(cls):
        pagesApi = groupdocs_merger_cloud.PagesApi.from_keys(Common.app_sid, Common.app_key)

        options = groupdocs_merger_cloud.RemoveOptions()
        options.file_info = groupdocs_merger_cloud.FileInfo("WordProcessing/four-pages.docx")
        options.output_path = "Output/remove-pages.docx"
        options.pages = [2, 4]

        result = pagesApi.remove(groupdocs_merger_cloud.RemoveRequest(options))

        print("Output file path = " + result.path)