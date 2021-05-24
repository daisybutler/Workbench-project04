from django.shortcuts import render
from .models import Plan


def all_plans(request):
    """A view to display all plans."""

    plans = Plan.objects.all()

    context = {
        'plans': plans,
    }

    return render(request, 'plans/plans.html', context)
