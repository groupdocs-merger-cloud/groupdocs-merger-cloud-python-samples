# Import modules
import groupdocs_merger_cloud
from Common import Common

# This example demonstrates how to join images
class JoinImages:
    @classmethod  
    def Run(cls):
        documentApi = groupdocs_merger_cloud.DocumentApi.from_config(Common.GetConfig())

        item1 = groupdocs_merger_cloud.JoinItem()
        item1.file_info = groupdocs_merger_cloud.FileInfo("Img/task1.jpg")
        item2 = groupdocs_merger_cloud.JoinItem()
        item2.file_info = groupdocs_merger_cloud.FileInfo("Img/task2.jpg")
        item2.image_join_mode = "Vertical"

        options = groupdocs_merger_cloud.JoinOptions()
        options.join_items = [item1, item2]
        options.output_path = "Output/joined.jpg"

        result = documentApi.join(groupdocs_merger_cloud.JoinRequest(options))        

        print("Output file path = " + result.path)