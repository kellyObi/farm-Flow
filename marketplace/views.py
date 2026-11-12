from django.shortcuts import render


def home(request):

    products = [
        {
            'name': 'Fresh Tomatoes',
            'category': 'Vegetables',
            'price': '2,500 FCFA',
            'location': 'Bamenda',
            'image': 'https://images.unsplash.com/photo-1546094096-0df4bcaaa337?w=500'
        },

        {
            'name': 'Fresh Carrots',
            'category': 'Vegetables',
            'price': '1,500 FCFA',
            'location': 'Bafoussam',
            'image': 'https://images.unsplash.com/photo-1445282768818-728615cc910a?w=500'
        },

        {
            'name': 'Fresh Corn',
            'category': 'Grains',
            'price': '3,000 FCFA',
            'location': 'Santa',
            'image': 'https://images.unsplash.com/photo-1551754655-cd27e38d2076?w=500'
        },

        {
            'name': 'Fresh Cabbage',
            'category': 'Vegetables',
            'price': '1,000 FCFA',
            'location': 'Bamenda',
            'image': 'https://images.unsplash.com/photo-1594282486552-05b4d80fbb9f?w=500'
        },
    ]

    return render(request, 'marketplace/home.html', {
        'products': products
    })