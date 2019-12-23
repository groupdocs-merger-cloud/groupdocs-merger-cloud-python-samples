# Import modules
import groupdocs_merger_cloud
from Common import Common

# Get your app_sid and app_key at https://dashboard.groupdocs.cloud (free registration is required).
Common.app_sid = "XXXX-XXXX-XXXX-XXXX"
Common.app_key = "XXXXXXXXXXXXXXXX"
Common.myStorage = "First Storage"

# Upload Sample Files
Common.UploadSampleFiles()

# Get Supported File Types
from GetSupportedFileTypes import GetSupportedFileTypes
GetSupportedFileTypes.Run()

# Get Document Info
from GetInfo import GetInfo
GetInfo.Run()

# Split To Multi-Page Documents
from DocumentOperations.SplitDocument.SplitToMultiPageDocuments import SplitToMultiPageDocuments
SplitToMultiPageDocuments.Run()

# Split To Single Pages
from DocumentOperations.SplitDocument.SplitToSinglePages import SplitToSinglePages
SplitToSinglePages.Run()

# Split To Single Pages By Range
from DocumentOperations.SplitDocument.SplitToSinglePagesByRange import SplitToSinglePagesByRange
SplitToSinglePagesByRange.Run()

# Split To Single Pages By Range With Filter
from DocumentOperations.SplitDocument.SplitToSinglePagesByRangeWithFilter import SplitToSinglePagesByRangeWithFilter
SplitToSinglePagesByRangeWithFilter.Run()

# Join Multiple Documents
from DocumentOperations.JoinMultipleDocuments import JoinMultipleDocuments
JoinMultipleDocuments.Run()

# Join Pages From Various Documents
from DocumentOperations.JoinPagesFromVariousDocuments import JoinPagesFromVariousDocuments
JoinPagesFromVariousDocuments.Run()

# Preview Document
from DocumentOperations.PreviewDocument import PreviewDocument
PreviewDocument.Run()

# Change Page Orientation
from PagesOperations.ChangePageOrientation import ChangePageOrientation
ChangePageOrientation.Run()

# Extract Pages By Numbers
from PagesOperations.ExtractPages.ExtractPagesByNumbers import ExtractPagesByNumbers
ExtractPagesByNumbers.Run()

# Extract Pages By Range
from PagesOperations.ExtractPages.ExtractPagesByRange import ExtractPagesByRange
ExtractPagesByRange.Run()

# Move Page
from PagesOperations.MovePage import MovePage
MovePage.Run()

# Remove Pages
from PagesOperations.RemovePages import RemovePages
RemovePages.Run()

# Rotate Pages
from PagesOperations.RotatePages import RotatePages
RotatePages.Run()

# Swap Pages
from PagesOperations.SwapPages import SwapPages
SwapPages.Run()

# Add Document Password
from SecurityOperations.AddDocumentPassword import AddDocumentPassword
AddDocumentPassword.Run()

# Check Document Password Protection
from SecurityOperations.CheckDocumentPasswordProtection import CheckDocumentPasswordProtection
CheckDocumentPasswordProtection.Run()

# Remove Document Password
from SecurityOperations.RemoveDocumentPassword import RemoveDocumentPassword
RemoveDocumentPassword.Run()

# Update Document Password
from SecurityOperations.UpdateDocumentPassword import UpdateDocumentPassword
UpdateDocumentPassword.Run()
