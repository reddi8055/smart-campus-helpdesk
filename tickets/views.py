from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Ticket
from .serializers import TicketSerializer
from django.views.decorators.cache import cache_page
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@cache_page(120)
def ticket_list(request):

    if request.method == 'GET':
        tickets = Ticket.objects.all()

        # Filtering
        status = request.query_params.get('status')
        title = request.query_params.get('title')

        if status:
            tickets = tickets.filter(status=status)

        if title:
            tickets = tickets.filter(title__icontains=title)

        # Pagination
        paginator = PageNumberPagination()
        paginator.page_size = 2
        result_page = paginator.paginate_queryset(tickets, request)

        serializer = TicketSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def ticket_detail(request, id):

    try:
        ticket = Ticket.objects.get(id=id)
    except Ticket.DoesNotExist:
        return Response({'error': 'Ticket not found'}, status=404)

    if request.method == 'GET':
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TicketSerializer(ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'PATCH':
        serializer = TicketSerializer(ticket, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        ticket.delete()
        return Response({'message': 'Ticket deleted successfully'}, status=204)