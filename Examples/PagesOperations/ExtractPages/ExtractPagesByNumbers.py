# Import modules
import groupdocs_merger_cloud
from Common import Common

# This example demonstrates how to extract document pages by specifying their numbers
class ExtractPagesByNumbers:
    @classmethod  
    def Run(cls):
        pagesApi = groupdocs_merger_cloud.PagesApi.from_config(Common.GetConfig())

        options = groupdocs_merger_cloud.ExtractOptions()
        options.file_info = groupdocs_merger_cloud.FileInfo("WordProcessing/sample-10-pages.docx")
        options.output_path = "Output/extract-pages-by-numbers.docx"
        options.pages = [2, 4, 7]        

        result = pagesApi.extract(groupdocs_merger_cloud.ExtractRequest(options))        

        print("Output file path = " + result.path)