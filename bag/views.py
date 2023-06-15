from django.shortcuts import render

# Create views


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')
