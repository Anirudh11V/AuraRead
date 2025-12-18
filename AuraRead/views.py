from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings

import io
import os
from pypdf import PdfReader, PdfWriter
from gtts import gTTS

from .models import PdfDocumnet
from .forms import PdfUploadForm, PageRangeForm

# Create your views here.

def Upload(request):
    form = PdfUploadForm()
    if request.method == 'POST':
        form = PdfUploadForm(request.POST, request.FILES)

        if form.is_valid():
            pdf_instance = form.save()
            return redirect('AuraRead:select_range', pdf_id= pdf_instance.id)
        
    return render(request, 'AuraRead/upload_pdf.html', {'form':form})


def select_range(request, pdf_id):
    pdf_instance = get_object_or_404(PdfDocumnet, id= pdf_id)

    if request.method == 'POST':
        form = PageRangeForm(request.POST)

        if form.is_valid():
            start_page = form.cleaned_data['start_page']
            end_page = form.cleaned_data['end_page']
            
            # CORE LOGIC: PDF Extraction
            extracted_text = extract_text_from_pdf(pdf_instance, start_page, end_page)

            if "ERROR" in extracted_text:
                return render(request, 'AuraRead/select_range.html', {'form': form, 'error': extracted_text})
        
            # Text to Audio (TTS)
            audio_filename = f'audio_{pdf_instance.id}.mp3'
            audio_path = os.path.join(settings.MEDIA_ROOT, 'audio', audio_filename)
            os.makedirs(os.path.dirname(audio_path), exist_ok= True)

            # Use gTTS 
            tts = gTTS(text= extracted_text, lang='en')
            tts.save(audio_path)

            pdf_instance.audio_file = f"audio/{audio_filename}"
            pdf_instance.save()

            # Redirect to final playback
            return redirect('AuraRead:listen_audio', pdf_id= pdf_instance.id)
        
    else:
        form = PageRangeForm(initial= {'pdf_id': pdf_id})

    context = {'pdf_id': pdf_id, 'form': form}
    return render(request, 'AuraRead/select_range.html', context)


def extract_text_from_pdf(pdf_instance, start_page, end_page):
    full_text = ""

    try:
        reader = PdfReader(pdf_instance.File.path)
        total_pages = len(reader.pages)

        # Adjust start / end
        start_index = max(0, start_page - 1)
        end_index = min(total_pages, end_page)

        for i in range(start_index, end_index):
            page = reader.pages[i]
            full_text += page.extract_text() + "\n\n"

        if start_page > end_page or end_page > total_pages:
            return f"Error: Invalid range (Total pages: {total_pages})"
        
    except Exception as e:
        print(f"ERROR: Could not read the PDF file.")

    return full_text


def listen_audio(request, pdf_id):
    pdf_document = get_object_or_404(PdfDocumnet, id= pdf_id)

    context = {'pdf': pdf_document, 'audio_url': pdf_document.audio_file.url if pdf_document.audio_file else None}
    return render(request, 'AuraRead/listen_audio.html', context)