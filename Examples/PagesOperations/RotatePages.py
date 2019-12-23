# Import modules
import groupdocs_merger_cloud
from Common import Common

# This example demonstrates how to rotate document pages
class RotatePages:
    @classmethod  
    def Run(cls):
        pagesApi = groupdocs_merger_cloud.PagesApi.from_keys(Common.app_sid, Common.app_key)

        options = groupdocs_merger_cloud.RotateOptions()
        options.file_info = groupdocs_merger_cloud.FileInfo("Pdf/ten-pages.pdf")
        options.output_path = "Output/rotate-pages.pdf"
        options.pages = [2, 4]
        options.mode = "Rotate90"

        result = pagesApi.rotate(groupdocs_merger_cloud.RotateRequest(options))

        print("Output file path = " + result.path)