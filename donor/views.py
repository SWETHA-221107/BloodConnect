from django.shortcuts import render, redirect
from .models import Donor, BloodRequest


def home(request):
    return render(request, 'home.html')


def register_donor(request):
    if request.method == 'POST':
        name = request.POST['name']
        blood_group = request.POST['blood_group']
        phone = request.POST['phone']
        city = request.POST['city']

        Donor.objects.create(
            name=name,
            blood_group=blood_group,
            phone=phone,
            city=city
        )

        return redirect('find_donors')

    return render(request, 'register_donor.html')


def find_donors(request):
    blood_group = request.GET.get('blood_group')

    if blood_group:
        donors = Donor.objects.filter(blood_group=blood_group)
    else:
        donors = Donor.objects.all()

    return render(request, 'find_donors.html', {
        'donors': donors
    })


def blood_request(request):
    if request.method == 'POST':
        blood_group = request.POST['blood_group']

        BloodRequest.objects.create(
            requester_name=request.POST['requester_name'],
            blood_group=blood_group,
            hospital=request.POST['hospital'],
            phone=request.POST['phone']
        )

        donors = Donor.objects.filter(blood_group=blood_group)

        return render(request, 'success.html', {
            'blood_group': blood_group,
            'donors': donors
        })

    return render(request, 'blood_request.html')
