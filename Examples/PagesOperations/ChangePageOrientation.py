# Import modules
import groupdocs_merger_cloud
from Common import Common

# This example demonstrates how to change document page orientation
class ChangePageOrientation:
    @classmethod  
    def Run(cls):
        pagesApi = groupdocs_merger_cloud.PagesApi.from_keys(Common.app_sid, Common.app_key)

        options = groupdocs_merger_cloud.OrientationOptions()
        options.file_info = groupdocs_merger_cloud.FileInfo("WordProcessing/four-pages.docx")
        options.output_path = "Output/change-page-orientation.docx"
        options.pages = [2, 4]
        options.mode = "Landscape"

        result = pagesApi.orientation(groupdocs_merger_cloud.OrientationRequest(options))        

        print("Output file path = " + result.path)