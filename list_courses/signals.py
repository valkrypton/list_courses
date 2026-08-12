import logging

from openedx_events.content_authoring.data import CourseData

logger = logging.getLogger(__name__)


def course_created_handler(signal, sender, course: CourseData, **kwargs):
    logger.info("Course Created: %s", course)
