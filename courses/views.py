from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Course
from .serializers import CourseSerializer
from users.permissions import IsInstructor, IsApprover

class CourseCreateView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsInstructor]

class CourseApprovalView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsApprover]

    def patch(self, request, *args, **kwargs):
        course = self.get_object()
        course.status = 'Approved'
        course.save()
        return Response({"status": "Course approved"})

class EnrollCourseView(generics.CreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]

class ProgressView(generics.RetrieveUpdateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]