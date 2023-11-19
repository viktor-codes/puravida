from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.utils import timezone
from .models import Coupon
from .forms import CouponApplyForm
from decimal import Decimal



@require_POST
def coupon_apply(request):
    print("View: coupon_apply were called")
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(
                code__iexact=code,
                valid_from__lte=now,
                valid_to__gte=now,
                active=True
            )
            request.session['coupon_id'] = coupon.id
            request.session['discount'] = coupon.discount
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
            request.session['coupon_applied'] = False
        
    return redirect('view_bag')
