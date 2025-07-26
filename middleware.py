from django.http import HttpResponseForbidden
class TierRequiredMiddleware:
    def __init__(self, get_response): self.get_response = get_response
    def __call__(self, request): return self.get_response(request)
def tier_required(min_tier):
    tiers = ["free", "basic", "student", "pro", "lab"]
    def decorator(view_func):
        def _wrapped(request, *args, **kwargs):
            user_tier = getattr(request.user, "membership_tier", "free")
            if tiers.index(user_tier) < tiers.index(min_tier):
                return HttpResponseForbidden("Upgrade required")
            return view_func(request, *args, **kwargs)
        return _wrapped
    return decorator
