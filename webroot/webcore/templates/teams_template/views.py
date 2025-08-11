from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_GET, require_http_methods, require_POST, require_safe
from django.shortcuts import render
from usercore.models import EmployeeUser, businessid
from django.db import transaction
from django.contrib.auth.models import Permission
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType

@login_required
def teams(request):
    return(render(request, 'teams_template/teams.html'))

@login_required
@never_cache
def new_team(request):
    if request.method == 'GET':
        business_id = request.user.businessid
        employees = EmployeeUser.objects.filter(businessid = business_id).values()
        content = {
            'employee_name_list':[],
            'employee_num_list':[],
        }
        for i in employees:
            content['employee_name_list'].append(i['first_name'])
            content['employee_num_list'].append(i['employeeid'])

        
        return(render(request, 'teams_template/new_team.html', content))
    else:
        return(render(request, 'teams_template/response/wrong_entry.html'))


@login_required
@never_cache
def new_member(request):
    business_id = request.user.businessid
    id = EmployeeUser.objects.filter(businessid_id = business_id).values()
    length = len(id)
    if length>0:
        id = id[length-1]['employeeid'] +1
    else:
        id = 1
    content = {'id': id}
    return(render(request, 'teams_template/new_member.html', content))


@login_required
@never_cache
def member_template(request):
    return(render(request, 'teams_template/member_template.html'))

@login_required
@never_cache
def team_template(request):
    return(render(request, 'teams_template/team_template.html'))

@login_required
@never_cache
def manage_teams(request):
    return(render(request, 'teams_template/manage_teams.html'))

@login_required
@never_cache
def manage_members(request):
    return(render(request, 'teams_template/manage_members.html'))

@login_required
@never_cache
def manage_attendance(request):
    return(render(request, 'teams_template/manage_attendance.html'))

##API views from here

@login_required
@never_cache
def get_package_number(request):
    return render(request,'')

@login_required
@never_cache
@require_POST
def store_package(request):
    return render(request, '')

@login_required
def adding_member(request):
    if request.method == 'POST':
        if request.headers.get('HX-Request') == 'true':
            try:
                employee_name = request.POST.get('employee_name')
                employee_phone = request.POST.get('employee_phone')
                employee_address = request.POST.get('employee_address')
                employee_is_admin = request.POST.get('employee_is_admin')            
                businessid = request.user.businessid
                password = request.POST.get('employee_password')
                id = EmployeeUser.objects.filter(businessid = request.user.businessid).values()
                length = len(id)
                print(length)
                if length>0:
                    id=id[length-1]['employeeid']+1

                content_type = ContentType.objects.get_for_model(EmployeeUser)
                permission = Permission.objects.get(codename='employee_is_admin', content_type=content_type)
                time = timezone.now()

                Employee_User = EmployeeUser(employeeid = id,
                                            businessid=businessid, 
                                            phone_contact=employee_phone,
                                            address=employee_address,
                                            first_name = employee_name,
                                            password=password,
                                            created_on=time  ,
                                            username = '00'+businessid.__str__()+'00'+id.__str__()
                                            )
                
                with transaction.atomic():
                    Employee_User.save()
                    if employee_is_admin:
                        Employee_User.user_permissions.add(permission)

                return render(request, 'teams_template/response/member_added.html')
            except Exception as e:
                print(e)
        return render(request, 'teams_template/response/wrong_entery.html')
