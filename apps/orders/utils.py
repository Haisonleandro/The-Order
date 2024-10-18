from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

def generar_factura(pedido):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.drawString(100, 750, f"Factura de Pedido #{pedido.id}")
    p.drawString(100, 730, f"Cliente: {pedido.cliente.nombre}")
    p.drawString(100, 710, f"Producto: {pedido.producto.nombre}")
    p.drawString(100, 690, f"Cantidad: {pedido.cantidad}")
    p.drawString(100, 670, f"Total: {pedido.producto.precio * pedido.cantidad}")
    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer
