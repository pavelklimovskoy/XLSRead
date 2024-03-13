import xlrd
from django.http import FileResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.files.storage import default_storage
from xlrd import Book
from xlrd.sheet import Sheet


class UploadFilesView(APIView):
    def post(self, request, format=None):
        file = request.FILES['file']

        workbook: Book = xlrd.open_workbook(
            file_contents=request.FILES['file'].read(),
            encoding_override="utf8"
        )

        worksheet: Sheet = workbook.sheet_by_index(0)

        for i in range(worksheet.nrows):
            for j in range(worksheet.row_len(i)):
                print(worksheet.cell_value(i, j), end='\t')
            print()

        return JsonResponse({'id': "new_file"})
