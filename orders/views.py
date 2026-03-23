from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Coupon
from django.utils import timezone


class CouponValidationView(APIView):
    def post(self, request):
        code = request.data.get("code")
    
        if not code:
            return Response(
                {"error": "Coupon code required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            coupon = Coupon.objects.get(code=code)
            today = timezone.now().date()
            if (
                coupon.is_active
                and coupon.valid_from <= today
                and coupon.valid_until >= today
            ):
                return Response(
                    {
                        "success": True,
                        "discount_percentage": coupon.discount_percentage
                    }
                )

            else:
                return Response(
                    {"error": "Coupon not valid"},
                    status=status.HTTP_400_BAD_REQUEST
                )

        except Coupon.DoesNotExist:
            return Response(
                {"error": "Coupon not found"},
                status=status.HTTP_404_NOT_FOUND
            )