from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .supabase_client import supabase


# 0. Dashboard View
def dashboard_view(request):
    return render(request, 'core/index.html')


# 1. Departments
class DepartmentListCreateView(APIView):
    def get(self, request):
        res = supabase.table("departments").select("*").execute()
        return Response(res.data, status=status.HTTP_200_OK)

    def post(self, request):
        res = supabase.table("departments").insert(request.data).execute()
        return Response(res.data, status=status.HTTP_201_CREATED)

class DepartmentDetailView(APIView):
    def get(self, request, pk):
        res = supabase.table("departments").select("*").eq("id", str(pk)).execute()
        return Response(res.data[0] if res.data else {}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        res = supabase.table("departments").update(request.data).eq("id", str(pk)).execute()
        return Response(res.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        supabase.table("departments").delete().eq("id", str(pk)).execute()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 2. Employees
class EmployeeListCreateView(APIView):
    def get(self, request):
        res = supabase.table("employees").select("*").execute()
        return Response(res.data, status=status.HTTP_200_OK)

    def post(self, request):
        res = supabase.table("employees").insert(request.data).execute()
        return Response(res.data, status=status.HTTP_201_CREATED)

class EmployeeDetailView(APIView):
    def get(self, request, pk):
        res = supabase.table("employees").select("*").eq("id", str(pk)).execute()
        return Response(res.data[0] if res.data else {}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        res = supabase.table("employees").update(request.data).eq("id", str(pk)).execute()
        return Response(res.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        supabase.table("employees").delete().eq("id", str(pk)).execute()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 3. Attendance
class AttendanceListCreateView(APIView):
    def get(self, request):
        res = supabase.table("attendance").select("*").execute()
        return Response(res.data, status=status.HTTP_200_OK)

    def post(self, request):
        res = supabase.table("attendance").insert(request.data).execute()
        return Response(res.data, status=status.HTTP_201_CREATED)

class AttendanceDetailView(APIView):
    def get(self, request, pk):
        res = supabase.table("attendance").select("*").eq("id", str(pk)).execute()
        return Response(res.data[0] if res.data else {}, status=status.HTTP_200_OK)

class AttendanceClockOutView(APIView):
    def post(self, request):
        emp_id = request.data.get("employee_id")
        clock_out_time = request.data.get("clock_out")
        res = supabase.table("attendance").update({"clock_out": clock_out_time}).eq("employee_id", emp_id).is_("clock_out", None).execute()
        return Response(res.data, status=status.HTTP_200_OK)


# 4. Leaves
class LeaveRequestListCreateView(APIView):
    def get(self, request):
        res = supabase.table("leaves").select("*").execute()
        return Response(res.data, status=status.HTTP_200_OK)

    def post(self, request):
        res = supabase.table("leaves").insert(request.data).execute()
        return Response(res.data, status=status.HTTP_201_CREATED)

class LeaveRequestDetailView(APIView):
    def get(self, request, pk):
        res = supabase.table("leaves").select("*").eq("id", str(pk)).execute()
        return Response(res.data[0] if res.data else {}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        res = supabase.table("leaves").update(request.data).eq("id", str(pk)).execute()
        return Response(res.data, status=status.HTTP_200_OK)


# 5. Shift Rosters
class ShiftRosterListCreateView(APIView):
    def get(self, request):
        res = supabase.table("shift_rosters").select("*").execute()
        return Response(res.data, status=status.HTTP_200_OK)

    def post(self, request):
        res = supabase.table("shift_rosters").insert(request.data).execute()
        return Response(res.data, status=status.HTTP_201_CREATED)

class ShiftRosterDetailView(APIView):
    def get(self, request, pk):
        res = supabase.table("shift_rosters").select("*").eq("id", str(pk)).execute()
        return Response(res.data[0] if res.data else {}, status=status.HTTP_200_OK)


# 6. Payroll Runs
class PayrollRunListCreateView(APIView):
    def get(self, request):
        res = supabase.table("payroll_runs").select("*").execute()
        return Response(res.data, status=status.HTTP_200_OK)

    def post(self, request):
        res = supabase.table("payroll_runs").insert(request.data).execute()
        return Response(res.data, status=status.HTTP_201_CREATED)

class PayrollRunDetailView(APIView):
    def get(self, request, pk):
        res = supabase.table("payroll_runs").select("*").eq("id", str(pk)).execute()
        return Response(res.data[0] if res.data else {}, status=status.HTTP_200_OK)


# 7. Payroll Items
class PayrollItemListCreateView(APIView):
    def get(self, request):
        res = supabase.table("payroll_items").select("*").execute()
        return Response(res.data, status=status.HTTP_200_OK)

    def post(self, request):
        res = supabase.table("payroll_items").insert(request.data).execute()
        return Response(res.data, status=status.HTTP_201_CREATED)

class PayrollItemDetailView(APIView):
    def get(self, request, pk):
        res = supabase.table("payroll_items").select("*").eq("id", str(pk)).execute()
        return Response(res.data[0] if res.data else {}, status=status.HTTP_200_OK)


# 8. Performance Reviews
class PerformanceReviewListCreateView(APIView):
    def get(self, request):
        res = supabase.table("performance_reviews").select("*").execute()
        return Response(res.data, status=status.HTTP_200_OK)

    def post(self, request):
        res = supabase.table("performance_reviews").insert(request.data).execute()
        return Response(res.data, status=status.HTTP_201_CREATED)

class PerformanceReviewDetailView(APIView):
    def get(self, request, pk):
        res = supabase.table("performance_reviews").select("*").eq("id", str(pk)).execute()
        return Response(res.data[0] if res.data else {}, status=status.HTTP_200_OK)


# 9. Audit Logs
class EmployeeAuditLogListView(APIView):
    def get(self, request):
        res = supabase.table("audit_logs").select("*").execute()
        return Response(res.data, status=status.HTTP_200_OK)