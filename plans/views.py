from django.shortcuts import render, get_object_or_404
from .models import Plan


def all_plans(request):

    """A view to display all plans."""

    plans = Plan.objects.all()

    context = {
        'plans': plans,
    }

    return render(request, 'plans/plans.html', context)


def individual_plan(request, name):
    
    """A view to display details of an individual plan."""

    plan = Plan.objects.get(name=name)

    context = {
        'plan': plan,
    }

    return render(request, 'plans/individual-plan.html', context)
