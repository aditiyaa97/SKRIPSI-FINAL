# Import module
import groupdocs_conversion_cloud
import sys

# Get your app_sid and app_key at https://dashboard.groupdocs.cloud (free registration is required).
app_sid = "2b55c442-7fec-4532-be89-e85331b8d4fa"
app_key = "1995db1d88086365535e819425902751"

# Create instance of the API
convert_api = groupdocs_conversion_cloud.ConvertApi.from_keys(app_sid, app_key)
file_api = groupdocs_conversion_cloud.FileApi.from_keys(app_sid, app_key)

try:
        #upload soruce file to storage
        filename = 'Proposal_Aditiya.pdf'
        remote_name = 'Proposal_Aditiya.pdf'
        output_name= 'Proposal_Aditiya.docx'
        strformat='docx'

        request_upload = groupdocs_conversion_cloud.UploadFileRequest(remote_name,filename)
        response_upload = file_api.upload_file(request_upload)
        #Convert PDF to Word document
        settings = groupdocs_conversion_cloud.ConvertSettings()
        settings.file_path =remote_name
        settings.format = strformat
        settings.output_path = output_name

        loadOptions = groupdocs_conversion_cloud.PdfLoadOptions()
        loadOptions.hide_pdf_annotations = True
        loadOptions.remove_embedded_files = False
        loadOptions.flatten_all_fields = True

        settings.load_options = loadOptions

        convertOptions = groupdocs_conversion_cloud.DocxConvertOptions()
        convertOptions.from_page = 1
        convertOptions.pages_count = 1

        settings.convert_options = convertOptions          
        request = groupdocs_conversion_cloud.ConvertDocumentRequest(settings)
        response = convert_api.convert_document(request)

        print("Document converted successfully: " + str(response))
except groupdocs_conversion_cloud.ApiException as e:
        print("Exception when calling get_supported_conversion_types: {0}".format(e.message))