from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def categoria(request,categoria):
    
    productos = {
        'electronica': [
            {'nombre': 'Smartphone', 'precio': 699.99},
                       {'nombre': 'Laptop', 'precio': 1299.99},
                       {'nombre': 'Auriculares', 'precio': 199.99}
                       ],
        'juguetes': [
            {'nombre': 'Muñeca', 'precio': 29.99},
                    {'nombre': 'Rompecabezas', 'precio': 14.99},
                    {'nombre': 'Pelota', 'precio': 9.99}
                    ],
        
        'ropa': [
            {'nombre': 'Camiseta', 'precio': 19.99},
                 {'nombre': 'Pantalones', 'precio': 39.99},
                 {'nombre': 'Zapatos', 'precio': 79.99}
                 ],
    }
    
    data = {
        'categoria': categoria,
        'productos': productos.get(categoria, [])
    }
    return render(request, 'categoria.html', data)
