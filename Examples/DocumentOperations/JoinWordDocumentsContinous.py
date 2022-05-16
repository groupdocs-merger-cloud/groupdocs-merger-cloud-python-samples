# Import modules
import groupdocs_merger_cloud
from Common import Common

# This example demonstrates how to join word document continously, without adding new page between documents
class JoinWordDocumentsContinous:
    @classmethod  
    def Run(cls):
        documentApi = groupdocs_merger_cloud.DocumentApi.from_config(Common.GetConfig())

        item1 = groupdocs_merger_cloud.JoinItem()
        item1.file_info = groupdocs_merger_cloud.FileInfo("WordProcessing/four-pages.docx")
        item2 = groupdocs_merger_cloud.JoinItem()
        item2.file_info = groupdocs_merger_cloud.FileInfo("WordProcessing/one-page.docx")
        item2.word_join_mode = "Continuous"

        options = groupdocs_merger_cloud.JoinOptions()
        options.join_items = [item1, item2]
        options.output_path = "Output/joined_continous.docx"

        result = documentApi.join(groupdocs_merger_cloud.JoinRequest(options))        

        print("Output file path = " + result.path)