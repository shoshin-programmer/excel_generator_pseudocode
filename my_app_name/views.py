from django.shortcuts import render
from django.urls import reverse
from .models import HRBP
from django.core.files.storage import default_storage
from django.conf import settings
from django.http import HttpResponse
import io
import os
import openpyxl
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
from openpyxl import load_workbook
from openpyxl.drawing.image import Image
from string  import ascii_uppercase as uppercase
import django_excel as excel
from django.conf import settings
from .forms import  < my forms here >
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font

def upload(request):
    if request.method == 'POST':
        form = urformherehrbpForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                try:
                    """ Placed deletion of database, and deletion of storage excel files
                    """
                except:
                    raise HttpResponse("Storage deletion error.")
                
                """ call a function to check deletion of storage media plots
                """
                filehandle = request.FILES['excel_reference']
                """
                Here I handled the file in memory into a pandas dataframe and an openpyxl object
                django-excel may or may not come in handy in this process, I used io for saving files into memory and then deleting them
                The project should be less than 2mb, if it is greater than that, you should use chunks in django files * see documentation
                """

                # format sheet
                sheet=book['Graph']
                sheet.column_dimensions['B'].width = 25
                sheet.column_dimensions['C'].width = 40
                for each in 'ABCDEFGHIJKLMNOP':
                    sheet.column_dimensions[each].width = 22
                for each_letter in uppercase:
                    for each in range(1,500):
                        sheet[f"{each_letter}{each}"].alignment = Alignment(horizontal='center')

                """ 

                called a function to add the images into the excel file
                getting plt into memory and saving it into the storage

                """
                writer.save()
                writer.close()

                form.save()
                # form = urformhere()
                # instance = <model instance and get the last>last()

                context = {
                    'form': form,
                    'object': instance.excel_reference.url,
                    'dict_html': <for dataframes>,
                    'images': for the graph,
                }
                return render(request, 'attrition_report/upload.html', context)
            except:
                form = urformhere()
                context = {
                    'errors': 'There was an error generating your report. Make sure you have selected the correct month and the correct file and check the formatting. Message developer if the problem persists.',
                    'form': form,
                }
                return render(request, 'attrition_report/upload.html', context=context)
        if form.is_valid():
            form = urformhere()
    else:
        form = urformhere()
    return render(request, 'attrition_report/upload.html', {'form':form})