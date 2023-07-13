import openpyxl
from django.http import HttpResponse


def export_to_excel(modeladmin, request, queryset):
    # Create a new workbook and get the active sheet
    workbook = openpyxl.Workbook()
    worksheet = workbook.active

    # Add headers to the worksheet
    headers = [field.verbose_name for field in modeladmin.model._meta.fields]
    for col_num, header in enumerate(headers, 1):
        cell = worksheet.cell(row=1, column=col_num)
        cell.value = header

    # Add data rows to the worksheet
    for row_num, obj in enumerate(queryset, 2):
        for col_num, field in enumerate(modeladmin.model._meta.fields, 1):
            value = str(getattr(obj, field.name))
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = value

    # Set the response headers for file download
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=data_entries.xlsx'

    # Save the workbook to the response
    workbook.save(response)

    return response
