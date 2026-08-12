from django.dispatch import receiver
import logging
from openedx_events.content_authoring.signals import COURSE_CREATED
from openedx_events.content_authoring.data import CourseData

logger = logging.getLogger(__name__)

@receiver(COURSE_CREATED)
def course_created_handler(signal, sender, course_data: CourseData, **kwargs):
    logger.info("Course Created: %s", course_data)
