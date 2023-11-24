from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.utils import timezone
from .models import Coupon
from .forms import CouponApplyForm
from django.contrib import messages


@require_POST
def coupon_apply(request):
    if request.method == 'POST':
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
                is_available = True if coupon else False
                is_active = coupon.active if coupon else False
                if is_available and is_active:
                    request.session['coupon_code'] = code
                    messages.info(
                        request, 'Your coupon was successfully applied!')
                else:
                    messages.error(request, 'Your coupon is invalid!')
            except Coupon.DoesNotExist:
                messages.error(request, 'Your coupon is invalid!')
    else:
        form = CouponApplyForm()
    referer = request.META.get('HTTP_REFERER', '/')

    return redirect(referer, {'form': form})
