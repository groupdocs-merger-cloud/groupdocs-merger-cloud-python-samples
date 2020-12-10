# Import modules
import groupdocs_merger_cloud
from Common import Common

# This example demonstrates how to split the document to several one-page documents (by start/end page numbers and even/odd filter)
class SplitToSinglePagesByRangeWithFilter:
    @classmethod  
    def Run(cls):
        documentApi = groupdocs_merger_cloud.DocumentApi.from_config(Common.GetConfig())

        options = groupdocs_merger_cloud.SplitOptions()
        options.file_info = groupdocs_merger_cloud.FileInfo("WordProcessing/sample-10-pages.docx")
        options.output_path = "Output/split-by-start-end-numbers-with-filter"
        options.start_page_number = 3
        options.end_page_number = 7
        options.range_mode = "OddPages"
        options.mode = "Pages"

        result = documentApi.split(groupdocs_merger_cloud.SplitRequest(options))        

        print("Documents count = " + str(len(result.documents)))