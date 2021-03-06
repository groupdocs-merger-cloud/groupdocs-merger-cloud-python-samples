# Import modules
import groupdocs_merger_cloud
from Common import Common

#  This example demonstrates how to obtain all supported file types
class GetSupportedFileTypes:
    @classmethod  
    def Run(cls):
        infoApi = groupdocs_merger_cloud.InfoApi.from_config(Common.GetConfig())
        result = infoApi.get_supported_file_formats()
        for format in result.formats:
            print(format.file_format)