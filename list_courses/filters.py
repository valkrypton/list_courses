from django.db.models import Q


def build_course_filters(title=None, language=None):
    filters = Q()
    if title:
        filters &= Q(display_name__icontains=title)
    if language:
        filters &= Q(language=language)
    return filters
