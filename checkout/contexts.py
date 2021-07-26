def purchase_contents(request):

    plan_purhases = []
    total = 0
    plan_count = 0

    context = {
        'plan_purhases': plan_purhases,
        'total': total,
        'plan_count': plan_count,
    }

    return context
