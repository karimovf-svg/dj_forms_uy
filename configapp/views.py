import qrcode
from io import BytesIO
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from .models import *
from .forms import StudentForm, FanlarForm

def index(request):
    student = Student.objects.all()
    subject = Fanlar.objects.all()

    context ={
        "student": student,
        "subject": subject,
        "title":"Najot Ta'lim",
    }
    return render(request,'index.html', context=context)

def fanlar_new(request, fan_id):
    student = Student.objects.filter(fan_id=fan_id)
    subject = Fanlar.objects.all()

    context = {
        "student": student,
        "subject": subject,
        "title": "Najot Ta'lim",
    }
    return render(request,'index.html', context=context)

def add_subject(request):
    if request.method == 'POST':
        form = FanlarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FanlarForm()
    return render(request, 'add_subject.html', {'form': form})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def student_del(request, student_id):
    if request.method == 'POST':
        student = get_object_or_404(Student, id=student_id)
        student.delete()
        return redirect(reverse('home'))

def generate_student_pdf(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{student.full_name}.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    # Sahifaning o'rtasini hisoblash
    center_x = width / 2
    center_y = height / 2


    p.setFont("Helvetica-Bold", 16)
    title = "Talaba Ma'lumotlari"
    title_width = p.stringWidth(title, "Helvetica-Bold", 16)
    p.drawString((width - title_width) / 2, height - 100, title)

    qr_link = "https://t.me/najottalim"

    qr = qrcode.make(qr_link)
    qr_io = BytesIO()
    qr.save(qr_io, format='PNG')
    qr_io.seek(0)
    qr_image = ImageReader(qr_io)

    if student.photo:
        student_image = ImageReader(student.photo.path)
        image_width = 300
        image_height = 300
        p.drawImage(student_image, (width - image_width) / 2, center_y - 50, width=image_width, height=image_height)
        center_y -= 120

    p.setFont("Helvetica", 12)
    info = [
        f"Ism: {student.full_name}",
        f"Telefon: {student.phone_number}",
        f"Manzil: {student.address}",
        f"Fan: {student.fan.title}"
    ]

    for line in info:
        line_width = p.stringWidth(line, "Helvetica", 12)
        p.drawString((width - line_width) / 2, center_y, line)
        center_y -= 20

    qr_width = 100
    qr_height = 100
    p.drawImage(qr_image, width - qr_width - 50, height - qr_height - 50, width=qr_width, height=qr_height)

    p.showPage()
    p.save()
    return response