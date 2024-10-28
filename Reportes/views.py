import io
from django.http import FileResponse, HttpResponse
from Citas.models import Cita
from reportlab.pdfgen import canvas
from reportlab.platypus import Table,TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
import datetime
from django.contrib.auth.decorators import login_required


@login_required
def reportepdf(request):
    date = datetime.datetime.now()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="date.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response, pagesize=letter)
    p.setTitle('Reporte Citas')
    p.setFont("Helvetica", 22)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(60, 750, "Reporte de Citas: "+str(date))
    # Define the width and height of each row in the table
    # row_height = 20
    # column_width = 100

    # Define the data to be printed in the table
    data = [
        ['Cliente', 'Fecha', 'Hora', 'Servicio', 'Barbero'],
    ]
    for obj in Cita.objects.all():
        data.append([obj.cliente, obj.cita, obj.hora, obj.servicio, obj.barbero])

    # # Draw the table
    # x = 50
    # y = 750
    # for row in data:
    #     for item in row:
    #         p.drawString(x, y, str(item))
    #         x += column_width
    #     x = 50
    #     y -= row_height


    table = Table(data)
    table.setStyle(TableStyle(
        [
        ('BACKGROUND', (0,0), (-1,0), colors.gray),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('ALIGN', (0, 0), (-1, -1), "CENTER")
        ]
    ))

    canvas_width = 600
    canvas_height = 600

    table.wrapOn(p, canvas_width, canvas_height)
    table.drawOn(p, 40, canvas_height - len(data))

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    return response