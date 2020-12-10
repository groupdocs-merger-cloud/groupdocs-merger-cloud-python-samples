# Import modules
import groupdocs_merger_cloud
from Common import Common

# This example demonstrates how to move document page to a new position
class MovePage:
    @classmethod  
    def Run(cls):
        pagesApi = groupdocs_merger_cloud.PagesApi.from_config(Common.GetConfig())

        options = groupdocs_merger_cloud.MoveOptions()
        options.file_info = groupdocs_merger_cloud.FileInfo("WordProcessing/four-pages.docx")
        options.output_path = "Output/move-pages.docx"
        options.page_number = 1
        options.new_page_number = 2        

        result = pagesApi.move(groupdocs_merger_cloud.MoveRequest(options))        

        print("Output file path = " + result.path)