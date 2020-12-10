# Import modules
import groupdocs_merger_cloud
from Common import Common

# This example demonstrates how to extract document pages by specifying page numbers range
class ExtractPagesByRange:
    @classmethod  
    def Run(cls):
        pagesApi = groupdocs_merger_cloud.PagesApi.from_config(Common.GetConfig())

        options = groupdocs_merger_cloud.ExtractOptions()
        options.file_info = groupdocs_merger_cloud.FileInfo("WordProcessing/sample-10-pages.docx")
        options.output_path = "Output/extract-pages-by-range.docx"
        options.start_page_number = 1
        options.end_page_number = 10
        options.range_mode = "EvenPages"      

        result = pagesApi.extract(groupdocs_merger_cloud.ExtractRequest(options))        

        print("Output file path = " + result.path)