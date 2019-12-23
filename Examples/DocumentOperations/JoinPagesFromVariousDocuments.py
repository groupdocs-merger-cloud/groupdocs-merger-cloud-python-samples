# Import modules
import groupdocs_merger_cloud
from Common import Common

# This example demonstrates how to join specific pages from several source documents
class JoinPagesFromVariousDocuments:
    @classmethod  
    def Run(cls):
        documentApi = groupdocs_merger_cloud.DocumentApi.from_keys(Common.app_sid, Common.app_key)

        item1 = groupdocs_merger_cloud.JoinItem()
        item1.file_info = groupdocs_merger_cloud.FileInfo("WordProcessing/sample-10-pages.docx")
        item1.pages = [3, 6, 8]
        
        item2 = groupdocs_merger_cloud.JoinItem()
        item2.file_info = groupdocs_merger_cloud.FileInfo("WordProcessing/four-pages.docx")
        item2.start_page_number = 1
        item2.end_page_number = 4
        item2.range_mode = "OddPages"

        options = groupdocs_merger_cloud.JoinOptions()
        options.join_items = [item1, item2]
        options.output_path = "Output/joined-pages.docx"

        result = documentApi.join(groupdocs_merger_cloud.JoinRequest(options))        

        print("Output file path = " + result.path)