# Import modules
import groupdocs_merger_cloud
from Common import Common

# This example demonstrates how to swap document pages
class SwapPages:
    @classmethod  
    def Run(cls):
        pagesApi = groupdocs_merger_cloud.PagesApi.from_keys(Common.app_sid, Common.app_key)

        options = groupdocs_merger_cloud.SwapOptions()
        options.file_info = groupdocs_merger_cloud.FileInfo("WordProcessing/four-pages.docx")
        options.output_path = "Output/swap-pages.docx"
        options.first_page_number = 2
        options.second_page_number = 4

        result = pagesApi.swap(groupdocs_merger_cloud.SwapRequest(options))

        print("Output file path = " + result.path)