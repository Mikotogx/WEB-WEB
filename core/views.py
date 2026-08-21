from rest_framework import generics
from django.shortcuts import render
from .models import (
    Department, Employee, Attendance, LeaveRequest, 
    ShiftRoster, PayrollRun, PayrollItem, PerformanceReview, EmployeeAuditLog
)
from .serializers import (
    DepartmentSerializer, EmployeeSerializer, AttendanceSerializer, 
    LeaveRequestSerializer, ShiftRosterSerializer, PayrollRunSerializer, 
    PayrollItemSerializer, PerformanceReviewSerializer, EmployeeAuditLogSerializer
)

# 0. Dashboard View (for the homepage root URL '')
def dashboard_view(request):
    return render(request, 'core/index.html')

# 1. Departments
class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

# 2. Employees
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# 3. Attendance
class AttendanceListCreateView(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class AttendanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class AttendanceClockOutView(generics.UpdateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

# 4. Leaves
class LeaveRequestListCreateView(generics.ListCreateAPIView):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer

class LeaveRequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer

# 5. Shift Rosters
class ShiftRosterListCreateView(generics.ListCreateAPIView):
    queryset = ShiftRoster.objects.all()
    serializer_class = ShiftRosterSerializer

class ShiftRosterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShiftRoster.objects.all()
    serializer_class = ShiftRosterSerializer

# 6. Payroll Runs
class PayrollRunListCreateView(generics.ListCreateAPIView):
    queryset = PayrollRun.objects.all()
    serializer_class = PayrollRunSerializer

class PayrollRunDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PayrollRun.objects.all()
    serializer_class = PayrollRunSerializer

# 7. Payroll Items
class PayrollItemListCreateView(generics.ListCreateAPIView):
    queryset = PayrollItem.objects.all()
    serializer_class = PayrollItemSerializer

class PayrollItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PayrollItem.objects.all()
    serializer_class = PayrollItemSerializer

# 8. Performance Reviews
class PerformanceReviewListCreateView(generics.ListCreateAPIView):
    queryset = PerformanceReview.objects.all()
    serializer_class = PerformanceReviewSerializer

class PerformanceReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PerformanceReview.objects.all()
    serializer_class = PerformanceReviewSerializer

# 9. Audit Logs
class EmployeeAuditLogListView(generics.ListAPIView):
    queryset = EmployeeAuditLog.objects.all()
    serializer_class = EmployeeAuditLogSerializer